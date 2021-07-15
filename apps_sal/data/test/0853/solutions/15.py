n = int(input())
seq = list(map(int, input().split()))

five = 0
zero = 0

for i in seq:
    if i == 5:
        five += 1
    elif i == 0:
        zero += 1

if five >= 9:
    mod = five % 9
    if zero >= 1:
        print((five - mod) * '5' + zero * '0')
    else:
        print(-1)
else:
    if zero > 0:
        print(0)
    else:
        print(-1)
