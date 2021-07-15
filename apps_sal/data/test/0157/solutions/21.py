a = int(input())
b = int(input())
c = int(input())
for i in range(1, 1000):
    if i <= a and i * 2 <= b and i * 4 <= c:
        continue
    else:
        break
print(i - 1 + (i - 1) * 2 + (i - 1) * 4)
