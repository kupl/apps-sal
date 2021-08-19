n = int(input())
is_leaf = [True] * (n + 1)
children = [[] for _ in range(n + 1)]
ans = 'Yes'
for i in range(2, n + 1):
    p = int(input())
    children[p].append(i)
    is_leaf[p] = False
for node in range(1, n + 1):
    if not is_leaf[node]:
        count = 0
        for child in children[node]:
            count += is_leaf[child]
        if count < 3:
            ans = 'No'
            break
print(ans)
