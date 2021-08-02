n = (int(input()))
edges = [0 for i in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    edges[x] += 1
    edges[y] += 1

leaves = []
node = None
flag = True
for i in range(1, n + 1):
    if(edges[i] == 1):
        leaves.append(i)
    elif(edges[i] > 2):
        if(not node == None):
            flag = False
            break
        else:
            node = i
if(flag):
    print("Yes")
    if(node == None):
        print(1)
        print(leaves[0], end=' ')
        print(leaves[1])
    else:
        print(len(leaves))
        for item in leaves:
            print(item, end=' ')
            print(node)
else:
    print("No")
