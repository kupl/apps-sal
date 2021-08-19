(n, k) = map(int, input().split())
a = list(map(int, input().split()))
p = [0]
for i in a[::-1]:
    p.append(p[-1] + i)
p = p[::-1]
ans = p[0]
ans += sum(sorted(p[1:-1], reverse=True)[:k - 1])
print(ans)
