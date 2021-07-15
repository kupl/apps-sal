__author__ = 'User'
n, m = list(map(int, input().split()))
cat = [0] + list(map(int, input().split()))
arr = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    arr[a].append(b)
    arr[b].append(a)
counter = [0] * n
c = 0
i = 0
queue = [(1, 0)]
#print(arr)
while i < len(queue):
    j = 0
    if len(arr[queue[i][0]]) == 1 and queue[i][1] == arr[queue[i][0]][0]:
        c += 1
    else:
        for j in arr[queue[i][0]]:
            if j != queue[i][1]:
                if cat[j] != 0:
                    cat[j] += cat[queue[i][0]]
                if cat[j] <= m:
                    queue.append((j, queue[i][0]))
    i += 1
print(c)
#print(queue)
#print(cat)
#print(arr)

