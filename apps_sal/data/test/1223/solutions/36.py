from bisect import bisect_left
import array

n = int(input())
p = []

for i, x in enumerate(map(int, input().split())):
    p.append([x, i])

p.sort(reverse=True)

s = array.array('i', [-1, -1, p[0][1], n, n])

# print(p)

ans = 0
i = 2
for a, x in p[1:]:
    t = bisect_left(s, x)
    ans += a * ((x - s[t - 1]) * (s[t + 1] - s[t]) + (s[t] - x) * (s[t - 1] - s[t - 2]))
    #print(t, s)
    s.insert(t, x)
    i += 1


print(ans)
