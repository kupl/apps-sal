from bisect import bisect

n = int(input())
array = [int(x) for x in input().split()]

tree = []
ans = [''] * n
for i in range(n):
    item = array[i]
    index = bisect(tree, (item, i))
    if i != 0:
        if index == 0:
            ans[i] = str(tree[0][0])
        elif index == i:
            ans[i] = str(tree[i - 1][0])
        else:
            ans[i] = str(tree[index - 1][0] if tree[index - 1][1] > tree[index][1] else tree[index][0])
    tree[index:index] = [(item, i)]
print(' '.join(ans[1:]))
