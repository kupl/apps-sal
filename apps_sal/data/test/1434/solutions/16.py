n = int(input())
stack_leaves = []
deg = [0]*n
s = [0]*n
summ = 0
for i in range(n):
    deg[i], s[i] = map(int, input().split())
    summ += deg[i]
    if deg[i] == 1:
        stack_leaves.append(i)
print(summ // 2)
while stack_leaves:
    x = stack_leaves.pop()
    if deg[x] != 0:
        print(x, s[x])
        deg[s[x]] -= 1
        s[s[x]] ^= x
        if deg[s[x]] == 1:
            stack_leaves.append(s[x])
