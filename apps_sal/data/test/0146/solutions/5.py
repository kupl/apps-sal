(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
mx = 0
for b in range(n):
    s = []
    for i in range(n):
        if abs(b - i) % k:
            s.append(l[i])
    mx = max(mx, abs(sum(s)))
print(mx)
