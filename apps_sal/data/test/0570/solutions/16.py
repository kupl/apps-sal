a, b = list(map(int, input().split()))

s = 0
cnt = 1
while True:
    if s % 2 == 0:
        if a < cnt:
            break
        a -= cnt
    else:
        if b < cnt:
            break
        b -= cnt
    cnt += 1
    s = 1 - s

print(["Vladik", "Valera"][s])
