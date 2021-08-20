n = int(input())
l = list(map(int, input().split()))
p = [0]
s = 0
for i in l:
    s += i
    p.append(s)
mx = 0
for i in range(1, n + 1):
    if p[i] > 100 * i:
        mx = max(mx, i)
    else:
        for j in range(i):
            if p[i] - p[j] > 100 * (i - j):
                mx = max(mx, i - j)
                break
print(mx)
