inp, k = list(map(int, input().split()))

inp = list(repr(inp))
ans = []

while len(inp) != 0:
    tmp = max(inp[:k + 1])
    pos = inp.index(tmp)
    k -= pos
    ans.append(tmp)
    inp.pop(pos)

print(''.join(ans))
