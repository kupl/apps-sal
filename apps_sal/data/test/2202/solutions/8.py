s = input().split()
(n, p) = (int(s[0]), int(s[1]))
cl = list(map(int, input().split()))
mx = 0
sm = sum(cl)
qs = cl[0]
for i in range(1, n):
    y = qs % p + (sm - qs) % p
    if y > mx:
        mx = y
    qs += cl[i]
print(mx)
