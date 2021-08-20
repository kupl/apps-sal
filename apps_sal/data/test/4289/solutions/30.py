n = int(input())
(t, a) = map(int, input().split())
H = list(map(int, input().split()))
p = 9999
m = 9999
for i in range(n):
    tem = t - H[i] * 0.006
    dist = abs(a - tem)
    if dist < m:
        p = H[i]
        m = dist
print(H.index(p) + 1)
