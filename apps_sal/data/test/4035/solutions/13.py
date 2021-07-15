a, b = list(map(int, input().split()))

for x in range(max(a, b), 2000):
    if x * 8 // 100 == a and x // 10 == b:
        print(x)
        return
print((-1))


