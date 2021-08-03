x = int(input())
year = 0
sum = 100

while sum < x:
    sum += int(sum // 100)
    year += 1

print(year)
