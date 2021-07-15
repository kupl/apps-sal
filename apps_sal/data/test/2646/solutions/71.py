n,m = map(int,input().split())
AB = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    AB[a-1].append(b-1)
    AB[b-1].append(a-1)

visited = set()
ans = [0]*n
stack = [0]
for i in stack:
    # このへんあやしい
    for j in AB[i]:
        if j in visited:
            continue
        visited.add(j)
        ans[j] = i+1
        stack.append(j)
    # このへんまで
for i in ans[1:]:
    if i==0:
        print('No')
        return
print('Yes')
for i in ans[1:]:
    print(i)
