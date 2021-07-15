n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

count = {}
for x in v:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

fact = [1] * 51
for i in range(1, 51):
    fact[i] = fact[i-1] * i

def comb(a, b):
    return fact[a] // fact[a-b] // fact[b]

ans = 0
if v[0] == v[a-1]:
    b = min(b, count[v[0]])
    for i in range(a, b+1):
        ans += comb(count[v[0]], i)
    print(v[0])
    print(ans)
else:
    c = v[:a].count(v[a-1])
    print(sum(v[:a]) / a)
    print(comb(count[v[a-1]], c))
