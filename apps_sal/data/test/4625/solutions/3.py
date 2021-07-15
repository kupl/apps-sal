import sys
input = sys.stdin.readline


alph = "abcdefghijklmnopqrstuvwxyz"
to_int = {v: i for i, v in enumerate(alph)}

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    s = input()
    p = list(map(int, input().split()))
    num = [[0] * (n + 1) for i in range(26)]
    for i in range(n):
        tmp = to_int[s[i]]
        for j in range(26):
            if tmp == j:
                num[j][i + 1] = num[j][i] + 1
            else:
                num[j][i + 1] = num[j][i]
    ans = [0] * 26
    for i in range(len(ans)):
        for j in p:
            ans[i] += num[i][j]
        ans[i] += num[i][-1]
    print(*ans)
