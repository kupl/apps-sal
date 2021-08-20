from bisect import bisect
n = int(input())
elements = list(map(int, input().split()))
tree = []
ans = [''] * n
for (i, x) in enumerate(elements):
    index = bisect(tree, (x, i))
    if i != 0:
        if index == 0:
            ans[i] = str(tree[0][0])
        elif index == i:
            ans[i] = str(tree[i - 1][0])
        elif tree[index - 1][1] < tree[index][1]:
            ans[i] = str(tree[index][0])
        else:
            ans[i] = str(tree[index - 1][0])
    tree[index:index] = [(x, i)]
print(' '.join(ans[1:]))
