K = int(input())
a = []

def DFS(n):
    if n > 3234566667:
        return
    a.append(n)
    l = n % 10
    if l == 0:
        DFS(10 * n)
        DFS(10 * n + 1)
    elif l == 9:
        DFS(10 * n + 9)
        DFS(10 * n + 8)
    else:
        DFS(10 * n + l)
        DFS(10 * n + l + 1)
        DFS(10 * n + l - 1)

for i in range(1, 10):
    DFS(i)

a = sorted(a)
print(a[K-1])
