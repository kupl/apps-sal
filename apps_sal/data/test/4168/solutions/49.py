N = int(input())
b = -2
temp = N
ans = ''
while True:
    if temp % b != 0:
        ans = '1' + ans
        temp = temp - b // -2
    else:
        ans = '0' + ans
    b = b * -2
    if temp == 0:
        break
print(ans)
