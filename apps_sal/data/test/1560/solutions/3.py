n = int(input())
m = input()
rb = {'r': 0, 'b': 0}
br = {'r': 0, 'b': 0}
for i in range(n):
    if i % 2:
        if m[i] == 'b':
            br['b'] += 1
        else:
            rb['r'] += 1
    elif m[i] == 'r':
        br['r'] += 1
    else:
        rb['b'] += 1
rbs = min(rb['b'], rb['r']) + abs(rb['b'] - rb['r'])
brs = min(br['b'], br['r']) + abs(br['b'] - br['r'])
print(min(rbs, brs))
