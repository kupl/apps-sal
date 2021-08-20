N = int(input())
a = list(map(int, input().split()))
color = [0] * 8
freer = 0
for i in a:
    if i < 3200:
        color[i // 400] += 1
    else:
        freer += 1
ans_base = 8 - color.count(0)
if ans_base == 0:
    ans_min = 1
else:
    ans_min = ans_base
ans_max = ans_base + freer
print(ans_min, ans_max)
