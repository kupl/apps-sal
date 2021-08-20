__author__ = 'ratnesh.mishra'
weights = list(map(int, input()))
weights = [cnt for (cnt, x) in enumerate(weights, 1) if x]
m = int(input())
state = [(0, 0, 0, [])]
res = 'NO'
while state:
    (w, b, k, l) = state.pop()
    if k == m:
        res = 'YES\n' + ' '.join(map(str, l))
        break
    for wt in weights:
        if wt != w and wt > b:
            state.append((wt, wt - b, k + 1, l + [wt]))
print(res)
