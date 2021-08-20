(n, t) = list(map(int, input().split()))
li = list(map(int, input().split()))
ad = 0
un = 0
mx = 0
for i in range(n):
    ad += li[i]
    if ad > t:
        ad -= li[un]
        un += 1
    mx = max(mx, i - un + 1)
print(mx)
