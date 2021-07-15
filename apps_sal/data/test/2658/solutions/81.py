n, k = map(int, input().split())
a = [-1] + list(map(int, input().split()))

visited = [0] * (1 + n)
curr = 1
while k:
    if visited[curr]:
        break
    else:
        visited[curr] = k
        curr = a[curr]
        k -= 1
        if k == 0:
            print(curr)
            return
repeat = visited[curr] - k
k = k % repeat
while k:
    curr = a[curr]
    k -= 1
print(curr)
