n = int(input())
l = [0] * n
r = [0] * n
num = [0] * 10000
for i in range(n):
    l[i], r[i] = list(map(int, input().split()))
    num[r[i]] += 1
ans = n
for i in range(n):
    if (num[l[i]] == 1) and (l[i] == r[i]): continue

    if (num[l[i]] < 1): continue
    ans -= 1

print(ans)
