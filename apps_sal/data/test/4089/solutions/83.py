def main(N):
    ans = None

    alphabets = []
    for i in range(97, 97 + 26):
        alphabets.append(chr(i))

    tmp = 0
    for i in range(1, 20):
        if tmp + 26**i >= N:
            break
        tmp += 26**i
    N -= tmp

    tmp = 0
    ans = []
    for j in range(1, i + 1):
        for k in range(26):
            if tmp + 26**(i - j) >= N:
                ans.append(k)
                break
            tmp += 26**(i - j)

    ans = ''.join([alphabets[id] for id in ans])

    return ans


def __starting_point():
    N = int(input())
    ans = main(N)
    print(ans)


__starting_point()
