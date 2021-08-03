n, c = list(map(int, input().split()))
tt = list(map(int, input().split()))

count = 0
pred = 0
for t in tt:
    if t - pred > c:
        count = 0
    count += 1
    pred = t
print(count)
