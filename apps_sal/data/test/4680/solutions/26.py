A, B, C = map(int, input().split())

num5 = 0
num7 = 0
ans = 'NO'

for num in [A, B, C]:
    if num == 5:
        num5 += 1
    elif num == 7:
        num7 += 1
    else:
        break
if num5 == 2 and num7 == 1:
    ans = 'YES'
print(ans)
