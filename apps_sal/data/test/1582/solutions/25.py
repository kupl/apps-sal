from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)


def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        if s[-1] == '0':
            continue
        if s[0] == s[-1]:
            ans += 1
        if i < 10:
            continue
        if s[0] == s[-1]:
            ans += 2
        l = len(s)
        for i in range(2, l):
            ans += 10 ** (i - 2) * 2
        if s[0] < s[-1]:
            continue
        if s[0] > s[-1]:
            ans += 10 ** (l - 2) * 2
        elif l > 2:
            dp = int(s[1])
            for i in range(2, l - 1):
                dp *= 10
                dp += int(s[i])
            ans += dp * 2
    print(ans)


main()
