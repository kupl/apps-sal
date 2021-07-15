from collections import deque

n, m, k = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

adj_dict = dict()
for i in range(1,n+1):
    adj_dict[i] = []
for i in range(m):
    u, v = [int(i) for i in input().split()]
    adj_dict[u].append(v)
    adj_dict[v].append(u)

size = [0 for i in range(k)]
remain = n
visited = set()
for i in range(k):
    subc = c[i]
    q = deque([subc])
    while q:
        cur = q[0]
        q.popleft()
        size[i] += 1
        remain -= 1
        visited.add(cur)
        for x in adj_dict[cur]:
            if x not in visited:
                q.append(x)
                visited.add(x)

size_list = sorted(size)
size_list[-1]+= remain
print(sum([ i*(i-1)//2 for i in size_list])-m)
