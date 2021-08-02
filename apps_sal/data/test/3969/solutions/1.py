from bisect import bisect_right
n = int(input().split()[0])
t = [int(input().split()[0]) for i in range(n)]
p, k = [], 0
for i in t:
    x = bisect_right(p, i)
    if x < k:
        p[x] = i
    else:
        p.append(i)
        k += 1
print(n - k)
