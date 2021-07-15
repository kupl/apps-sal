input()

def gcd(a,b):
    x,y = a,b
    while x:
        x, y = y % x, x
    return y

numbers = list(map(int, input().split()))

div = numbers[0]
for x in numbers:
    div = gcd(div, x)

for x in numbers:
    x = x / div
    while x % 3 == 0:
        x = x / 3
    while x % 2 == 0:
        x = x / 2
    if x != 1:
        print("No")
        return

print("Yes")

