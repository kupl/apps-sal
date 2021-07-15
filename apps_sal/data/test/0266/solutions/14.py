m, s = list(map(int, input().split()))

min_num = [0] * m
if s == 0 and m == 1:
    print('0 0')
    return
if s == 0 or s > m * 9:
    print("-1 -1")
    return

ci = len(min_num) - 1
s1 = s
while s > 0:
    a = min(9, s)
    s -= a
    min_num[ci] = a

    ci -= 1


if min_num[0] == 0:
    min_num[0] = 1
    for i in range(1, len(min_num)):
        if min_num[i] > 0:
            min_num[i] -= 1
            break

max_num = [0] * m
ci = 0

while s1 > 0:
    a = 9 if s1 >= 9 else s1
    s1 -= a

    max_num[ci] = a

    ci += 1

print("".join(map(str, min_num)), "".join(map(str, max_num)))



