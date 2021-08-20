def add(i, b):
    if i:
        return '-' + str(b)
    else:
        return '+' + str(b)


def main():
    S = input()
    (a, b, c, d) = (int(S[0]), int(S[1]), int(S[2]), int(S[3]))
    ans = ''
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if a + (-1) ** i * b + (-1) ** j * c + (-1) ** k * d == 7:
                    ans += str(a)
                    ans += add(i, b)
                    ans += add(j, c)
                    ans += add(k, d)
                    ans += '=7'
                    print(ans)
                    return


main()
