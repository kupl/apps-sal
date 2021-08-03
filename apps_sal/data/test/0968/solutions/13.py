false = False
curr = []
names = int(input())
ppl = [input().split(' ') for i in range(names)]
order = list(map(str, input().split(' ')))
for i in range(names):
    if i == 0:
        curr.append(min(ppl[int(order[i]) - 1]))
    else:
        a = ppl[int(order[i]) - 1][0]
        b = ppl[int(order[i]) - 1][1]
        if curr[-1] <= min(a, b):
            curr.append(min(a, b))
        elif curr[-1] <= max(a, b):
            curr.append(max(a, b))
        else:
            false = True
if false:
    print("NO")
else:
    print("YES")
