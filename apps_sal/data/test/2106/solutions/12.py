a, b = list(map(int, input().split()))
d = list(map(int, input().split()))
p = list(map(int, input().split()))
t = 0; d1 = 0; i = 0
while i < a:
    if t + sum(p[i::]) - sum(d[i::]) < 0:
        j = i; pr = p[i]
        while j < a and pr >= p[j]: j += 1
        k = (-t - sum(p[i:j]) - 1 + sum(d[i:j]) + pr) // pr
        d1 += b * k
        t = (pr * k - (-t - sum(p[i:j]) + sum(d[i:j]))) % pr
        i = j
    else: i += 1
print(sum(d) + d1)
