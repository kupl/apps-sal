import re

n = int(input())
for i in range(n):
    s = input()
    ones = [m.start() for m in re.finditer('one', s)]
    twos = [m.start() + 2 for m in re.finditer('two', s)]
    onei = 0
    twoi = 0
    ans = []
    while onei < len(ones) or twoi < len(twos):
        if onei < len(ones) and twoi < len(twos) and ones[onei] == twos[twoi]:
            ans.append(ones[onei])
            onei += 1
            twoi += 1
        elif onei == len(ones) or twoi == len(twos):
            if onei == len(ones):
                ans.append(twos[twoi] - 1)
                twoi += 1
            else:
                ans.append(ones[onei] + 1)
                onei += 1
        else:
            if twos[twoi] < ones[onei]:
                ans.append(twos[twoi] - 1)
                twoi += 1
            else:
                ans.append(ones[onei] + 1)
                onei += 1

    print(len(ans))
    for an in ans:
        print(an + 1, end=' ')
    print()


