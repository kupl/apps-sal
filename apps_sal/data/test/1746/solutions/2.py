n = int(input())
par = [-1 for i in range(n + 123)]
for i in range(2, n + 1):
    par[i] = int(input())
is_leaf = [True for i in range(n + 123)]
for i in range(2, n + 1):
    is_leaf[par[i]] = False
children = [0 for i in range(n + 123)]
for i in range(2, n + 1):
    children[par[i]] += is_leaf[i]
ans = True
for i in range(1, n + 1):
    if is_leaf[i]:
        continue
    ans &= children[i] >= 3
print('Yes' if ans else 'No')
