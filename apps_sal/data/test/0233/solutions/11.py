n = int(input())
num = 0
num2 = 0
while n > 0:
    n -= 1
    m, c = list(map(int, input().split()))
    if m > c:
        num += 1
    elif c > m:
        num2 += 1
if num > num2:
    print("Mishka")
elif num2 > num:
    print("Chris")
else:
    print("Friendship is magic!^^")
