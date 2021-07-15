tokens = input().split(',')

depths = []
stk = [len(tokens)]

for i in range(len(tokens)//2):
    tok = tokens[2*i]
    children = int(tokens[2*i+1])

    y = stk.pop()
    y -= 1
    stk.append(y)

    while len(depths) <= len(stk):
        depths.append([])
    depths[len(stk)].append(tok)
    stk.append(children)

    while stk and stk[-1] == 0:
        stk.pop()

print(len(depths)-1)
for xs in depths[1:]:
    print(' '.join(xs))


