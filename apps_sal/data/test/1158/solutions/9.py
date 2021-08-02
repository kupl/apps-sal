n, k = list(map(int, input().split()))
prib = list(map(int, input().split()))
prib.sort()
I = 0
p = []
while I < n:
    a = prib[I]
    p.append(0)
    while I < n and a == prib[I]:
        I += 1
        p[-1] += 1
p.sort()
l = (p[-1] - 1) // k + 1
l *= k
ans = 0
for i in p:
    ans += l - i
print(ans)
