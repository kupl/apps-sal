(n, m, ta, tb, k) = map(int, input().split())
fa = list(map(int, input().split()))
fb = list(map(int, input().split()))
flighta = 0
flightb = 0
for i in range(n):
    fa[i] += ta
ans = 0
while k >= 0:
    if flighta == n or flightb == m:
        print(-1)
        quit()
    if fb[flightb] < fa[flighta]:
        flightb += 1
        continue
    if k == 0:
        ans = max(ans, fb[flightb])
        break
    if flightb + k >= m:
        print(-1)
        quit()
    ans = max(fb[flightb + k], ans)
    flighta += 1
    k -= 1
print(ans + tb)
