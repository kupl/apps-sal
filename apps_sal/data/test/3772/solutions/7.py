
a, b = list(map(int, input().split()))
count = 0
while a > 0 and b > 0:
    if a > b:
        count += (a // b)
        a = a % b
    elif a < b:
        count += (b // a)
        b = (b % a)
    else:
        count += a
        a = b = 0
print(count)
