(n, k) = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for x in range(k + 1):
    for y in range(k - x + 1):
        temp = v[:x] + v[len(v) - y:]
        if x + y >= n:
            temp = v
        temp1 = []
        temp2 = []
        for i in temp:
            if i >= 0:
                temp1.append(i)
            else:
                temp2.append(i)
        temp2.sort()
        ans = max(ans, sum(temp1) + sum(temp2[k - x - y:]))
print(ans)
