(n, m) = map(int, input().split())
initial = []
first = input().split()
for i in range(n):
    initial.append(int(first[i]))
rest = []
for i in range(m - 1):
    current = []
    nfirst = input().split()
    for j in range(n):
        current.append(int(nfirst[j]))
    rest.append(current)
index = 0
compar = 0
ans = 0
indices = []
for i in range(m - 1):
    temp = [0] * n
    x = rest[i]
    for j in range(n):
        temp[x[j] - 1] = j
    indices.append(temp)
while index < n:
    compar = initial[index]
    cur = [0] * (m - 1)
    count = 1
    lol = n - index
    for k in range(m - 1):
        cur[k] = indices[k][compar - 1]
        lol = min(lol, n - cur[k])
    done = False
    while count < lol:
        for k in range(m - 1):
            x = rest[k]
            j = cur[k]
            if x[j + count] != initial[index + count]:
                done = True
                break
        if done:
            break
        count += 1
    ans += count * (count + 1) // 2
    index += count
print(ans)
