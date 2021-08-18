n = int(input())
parents = []
tree = [[] for i in range(n)]
for i in range(n - 1):
    par = int(input()) - 1
    tree[par].append(i + 1)
    parents.append(par)
flag = True
for i in parents:
    count = 0

    for j in tree[i]:
        if(len(tree[j]) == 0):
            count += 1
    if(count < 3):
        flag = False


if(flag):
    print('Yes')
else:
    print('No')
