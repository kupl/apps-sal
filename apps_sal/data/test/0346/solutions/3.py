[n, m], q, a = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
ans = sum(q[x - 1] for x in set(range(1, n + 1)) - set(a))
for x in sorted(a, key=lambda x: q[x - 1], reverse=True):
    if q[x - 1] <= ans:
        ans <<= 1
    else:
        ans += q[x - 1]
print(ans)
