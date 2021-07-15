a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
arr = [b + a * i for i in range(1000)]
for i in range(1000):
    if d + c * i in arr:
        print(d + c * i)
        return
print(-1)

