import bisect

N = int(input())
c = list(input())
c_sorted = sorted(c)

R_count = bisect.bisect_right(c_sorted, 'R')
ans = 0
for i in range(R_count):
    if c[i] != 'R':
        ans += 1
print(ans)
