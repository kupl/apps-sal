(N, M) = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
tmp = 0
for i in A:
    tmp += i
    B.append(tmp)
d = {}
for i in B:
    i %= M
    if i not in d:
        d[i] = 0
    d[i] += 1
ans = 0
for i in d.values():
    ans += i * (i - 1) // 2
print(ans)
