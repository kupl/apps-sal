ans = 0
n = int(input())
p = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(n):
    b[p[i]] = i + 1
LL = [0] + [i for i in range(n + 1)]
RR = [i for i in range(1, n + 2)] + [n + 1]
for i in range(1, n + 1):
    l1 = LL[b[i]]
    l0 = LL[l1]
    r0 = RR[b[i]]
    r1 = RR[r0]
    ans += ((l1 - l0) * (r0 - b[i]) + (r1 - r0) * (b[i] - l1)) * i
    LL[r0] = l1
    RR[l1] = r0
print(ans)
