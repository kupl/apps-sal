A, B = map(int, input().split())

# 任意の偶数に関して、n ^ (n+1) = 1
# nが偶数の時最下位ビットのみが異なるので。

num = B - A + 1
ans = 0

if A % 2 == 0:
    ones = num // 2

    if ones % 2 == 1:
        ans = 1
    else:
        ans = 0

    if num % 2 == 1:
        ans = ans ^ B

if A % 2 == 1:
    num -= 1

    ones = num // 2

    if ones % 2 == 1:
        ans = 1
    else:
        ans = 0

    if num % 2 == 1:
        ans = ans ^ B

    ans = ans ^ A

print(ans)
