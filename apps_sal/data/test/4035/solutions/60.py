a, b = list(map(int, input().split()))

for i in range(13, 1250):
    if i // 12.5 == a and i // 10 == b:
        print(i)
        return
print((-1))
