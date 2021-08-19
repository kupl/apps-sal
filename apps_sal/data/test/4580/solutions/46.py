n = int(input())
arr = list(map(int, input().split()))
colors = [0] * 8
over = 0
for i in arr:
    if i >= 3200:
        over += 1
    else:
        colors[i // 400] += 1
res = 8 - colors.count(0)
if res:
    print(res, res + over)
else:
    print(1, over)
