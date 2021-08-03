x = int(input())
count = 0
m = 100
while m < x:
    m += m // 100
    count += 1
print(count)
