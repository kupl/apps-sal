(n, t) = list(map(int, input().split()))
arr = list(map(int, input().split()))
c = 0
for i in arr:
    t -= 86400 - i
    c += 1
    if t <= 0:
        break
print(c)
