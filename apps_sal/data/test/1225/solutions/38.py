h = int(input())
count = 0
for i in range(40):
    count += 2**i
    if h >= 2 ** i and h < 2 ** (i + 1):
        break
print(count)
