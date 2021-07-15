n = int(input())
count = 0
for i in range(1, n+1):
    number = list(str(i))
    if len(number) % 2 != 0:
        count += 1
print(count)

