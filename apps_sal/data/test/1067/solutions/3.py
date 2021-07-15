n = int(input())
a = [int(item) for item in input().split()]
ans = 0
minus_cnt = 0
includes_zero = False
for item in a:
    if item == 0:
        includes_zero = True
        ans += 1
    elif item <= -1:
        minus_cnt += 1
        ans += -1 - item
    else:
        ans += item - 1
if includes_zero:
    print(ans)
elif minus_cnt % 2 == 0:
    print(ans)
else:
    print(ans + 2)
