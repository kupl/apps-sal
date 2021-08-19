N = int(input())
inputs = [tuple(map(int, input().split(' '))) for i in range(N)]
inputs = sorted(inputs, key=lambda x: x[1])
time = 0
for (ai, bi) in inputs:
    time += ai
    if time > bi:
        print('No')
        break
if time <= bi:
    print('Yes')
