a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

for i in range(0, 10000):
    if b + a * i >= d and (b + a * i - d) % c == 0:
        print(b + a * i)
        return
print(-1)
