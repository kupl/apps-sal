a, b = list(map(int, input().split()))
n = 0
while not (a == 0 or b == 0):
    if a > b:
        n += a // b
        a = a % b
    else:
        n += b // a
        b = b % a
print(n)
