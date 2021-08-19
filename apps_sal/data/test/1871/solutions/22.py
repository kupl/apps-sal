[n, x] = [int(i) for i in input().split()]
c = sorted([int(i) for i in input().split()])
time = 0
k = 0
while k < len(c):
    time += x * c[k]
    if x > 1:
        x -= 1
    k += 1
print(time)
