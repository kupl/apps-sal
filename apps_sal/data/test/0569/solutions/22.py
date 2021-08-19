import random


def __starting_point():
    #n, m = list(map(int, input().split()))
    n = int(input())
    s = input()
    if n > 26:
        print(-1)
    else:
        a = [0] * 26
        cnt = 0
        for i in range(n):
            if a[ord(s[i]) - ord('a')]:
                cnt += 1
            else:
                a[ord(s[i]) - ord('a')] = 1
        print(cnt)


__starting_point()
