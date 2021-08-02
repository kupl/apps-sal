n = int(input())
a = list(map(int, input().split()))
rate = [0, 399, 799, 1199, 1599, 1999, 2399, 2799, 3199, 4800]
cnt = [0] * 9

for i in a:
    for j in range(1, len(rate) + 1):
        if rate[j - 1] < i <= rate[j]:
            cnt[j - 1] += 1

fix = 0
flex = 0
for i, result in enumerate(cnt):
    if i == 8:
        flex = cnt[i]
    elif result > 0:
        fix += 1

if fix == 0 and flex >= 1:
    print(1, flex)
else:
    print(fix, fix + flex)
