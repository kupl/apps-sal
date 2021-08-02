x = int(input())
max = 0
total = 0
for i in range(1, x + 1):
    total += i
    if total >= x:
        max = i
        break
print(max)
