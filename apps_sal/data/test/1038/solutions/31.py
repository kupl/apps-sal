(A, B) = map(int, input().split())
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
