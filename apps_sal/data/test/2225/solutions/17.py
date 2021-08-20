import sys
(n, m) = list(map(int, sys.stdin.readline().lstrip().rstrip().split()))
arr = list(map(int, sys.stdin.readline().lstrip().rstrip().split()))
tree = [arr[:]]
cnt = 1
while True:
    temp = []
    ans = tree[-1]
    if len(ans) == 1:
        break
    else:
        if cnt % 2 != 0:
            for i in range(0, len(ans), 2):
                temp.append(ans[i] | ans[i + 1])
        else:
            for i in range(0, len(ans), 2):
                temp.append(ans[i] ^ ans[i + 1])
        tree.append(temp)
    cnt += 1
for i in range(m):
    (pos, val) = list(map(int, sys.stdin.readline().lstrip().rstrip().split()))
    pos -= 1
    tree[0][pos] = val
    cnt = 1
    while cnt <= n:
        pos = pos // 2
        if cnt % 2 != 0:
            tree[cnt][pos] = tree[cnt - 1][2 * pos] | tree[cnt - 1][2 * pos + 1]
        else:
            tree[cnt][pos] = tree[cnt - 1][2 * pos] ^ tree[cnt - 1][2 * pos + 1]
        cnt += 1
    sys.stdout.write(str(tree[-1][0]) + '\n')
