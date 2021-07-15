n = int(input())
ps = list(map(int, input().split()))
qs = list(map(int, input().split()))

maxi = 0
s_a, s_b = 0, 0
for l in range(n):
    s_a = ps[l]
    s_b = qs[l]
    for r in range(l, n):
        s_a = s_a | ps[r]
        s_b = s_b | qs[r]
        maxi = max(maxi, s_a + s_b)

print(maxi)

