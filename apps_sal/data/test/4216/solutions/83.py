import math
bb = int(input())
mini = bb
aa = int(math.sqrt(bb))
for i in range(1, aa + 1):
    if bb % i == 0:
        cc = int(bb / i)

        ans = len(str(cc))
        if ans < mini:
            mini = ans
print(mini)
