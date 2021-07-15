inp = [[int(x) for x in input().split()] for _ in range(int(input()))]
inpsum = sum(map(lambda ij: abs(ij[0]+ij[1]) % 2, inp))
if not (inpsum == len(inp) or inpsum == 0):
    print(-1)
    return

seeds = ([] if inpsum == len(inp) else [1]) + [1 << i for i in range(0, 32)]
# print(inp)

print(len(seeds))
print(' '.join(map(str, reversed(seeds))))

for x, y in inp:
    for k in reversed(seeds):
        res = ''
        if abs(x) > abs(y):
            if x > 0:
                res = 'R'
                x -= k
            else:
                res = 'L'
                x += k
        else:
            if y > 0:
                res = 'U'
                y -= k
            else:
                res = 'D'
                y += k
        # print((x,y))
        print(res, end='')
    print('')

