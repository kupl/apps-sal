def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


def main():
    n, m = list(map(int, input().split()))
    strings = []
    for i in range(n):
        strings.append(input())

    pairs = []
    alone = []
    for i in range(n):
        found = False
        s1 = strings[i]
        for j in range(i + 1, n):
            s2 = strings[j][::-1]
            # print(s1,s2)
            if s1 == s2:
                found = True
                pairs.append((s1, strings[j]))
                break

        if not found:
            if palindrome(s1):
                alone.append(s1)

    # print(pairs)
    s = ''
    for i in pairs:
        s += i[0]

    while len(alone) > 1:
        alone.pop()

    for i in alone:
        s += i

    pairs.reverse()
    for i in pairs:
        s += i[1]

    print(len(s))
    print(s)


main()
