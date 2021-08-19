(n, x) = map(int, input().split())
l = list(map(int, input().split()))
ball = 0
c = 1
for i in range(n):
    ball += l[i]
    if ball <= x:
        c += 1
    else:
        break
print(c)
