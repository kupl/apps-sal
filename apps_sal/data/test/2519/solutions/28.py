n, k = map(int, input().split())
p = list(map(int, input().split()))
q = [0]
m = 0
for i in p:
    m += (1 + i) / 2
    q.append(m)
ans = 0
for i in range(k, n + 1):
    ans = max(q[i] - q[i - k], ans)

# あまり深く事を考えずに
print(ans)
