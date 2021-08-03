import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
s = input()
ans = []


def f(i, j):
    if i == 0:
        print(" ".join(map(str, ans[::-1])))
        return
    if j > i:
        j = i
    while s[i - j] == "1":
        j -= 1
    if j == 0:
        print(-1)
        return
    ans.append(j)
    f(i - j, m)


f(n, m)
