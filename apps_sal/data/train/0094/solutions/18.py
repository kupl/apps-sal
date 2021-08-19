import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


for _ in range(int(input())):
    #n = int(input())
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    ans = [-1] * n
    for i in d.keys():
        if ans[d[i][0]] == -1:
            if i == t // 2:
                for j in range(len(d[i]) // 2):
                    ans[d[i][j]] = 0
                for j in range(len(d[i]) // 2, len(d[i])):
                    ans[d[i][j]] = 1
            else:
                for j in range(len(d[i])):
                    ans[d[i][j]] = 0
                if t - i in d:
                    for j in range(len(d[t - i])):
                        ans[d[t - i][j]] = 1
    for i in ans:
        print(i, end=' ')
    print('')
