n = int(input())
l = list(map(int, input().split()))
s = sum(l)
lo = s//n
hi = s//n + 1
lo_n = -1
for i in range(len(l)+1):
    if lo*i + hi*(len(l)-i) == s:
        lo_n = i
        break
if lo_n < 0 or lo_n > len(l):
    assert(False)
hi_n = n-lo_n
l = sorted(l)
l2 = []
for i in range(lo_n):
    l2.append(lo)
for i in range(hi_n):
    l2.append(hi)
ans = 0
for i in range(len(l)):
    ans += abs(l[i]-l2[i])
print(ans//2)

