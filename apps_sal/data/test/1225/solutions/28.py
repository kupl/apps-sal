import math

H = int(input())
ans = 0
num = 0

while True:
    ans += 2**num
    if H == 1:
        print(ans)
        break
    else:
        H = math.floor(H / 2)
        num += 1
