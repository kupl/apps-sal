def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = j + j - i
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                cnt += 1
    ans = r * g * b - cnt
    print(ans)


def __starting_point():
    main()


__starting_point()
