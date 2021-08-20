from collections import defaultdict
a = input()
b = input()


def form(a_digits):
    answer = []
    for i in sorted(a_digits, reverse=True):
        answer.append(i * a_digits[i])
    return ''.join(answer)


def main():
    if len(b) > len(a):
        return ''.join(sorted(list(a), reverse=True))
    else:
        a_digits = defaultdict(int)
        for x in a:
            a_digits[x] += 1
        r = 0
        for x in b:
            if a_digits[x] > 0:
                a_digits[x] -= 1
                r += 1
            else:
                for i in range(r, -1, -1):
                    for j in range(int(b[i]) - 1, -1, -1):
                        if a_digits[str(j)] > 0:
                            a_digits[str(j)] -= 1
                            return b[:i] + str(j) + form(a_digits)
                    a_digits[b[i - 1]] += 1
        return b


print(main())
