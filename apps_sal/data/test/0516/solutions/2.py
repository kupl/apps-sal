n, m = map(int, input().split())
s = input()
t = input()
ansC = 10 ** 9
ans = []
i = 0
while i < m - n + 1:
    nowc = 0
    now = []
    for j in range(n):
        if s[j] == t[i + j]:
            continue
        nowc += 1
        now.append(j + 1)
    if nowc < ansC:
        ansC = nowc
        ans = now[:]
    i += 1
print(ansC)
print(*ans)
