n = int(input())
sum = 0
for j in range(n):
    (i, c) = input().split()
    if c == 'BTC':
        sum += float(i) * 380000
    else:
        sum += int(i)
print(sum)
