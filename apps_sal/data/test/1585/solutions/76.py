def LI():
    return list(map(int, input().split()))


X, Y = LI()
count = 1
total = X
for i in range(1000000):
    total *= 2
    if total > Y:
        break
    count += 1
print(count)

