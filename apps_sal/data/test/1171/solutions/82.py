n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for x in range(k + 1):
    for y in range(k - x + 1):
        temp1 = []
        temp2 = []
        if x + y >= n:
            for i in v:
                if i >= 0:
                    temp1.append(i)
                else:
                    temp2.append(i)
        else:
            for i in v[:x]:
                if i >= 0:
                    temp1.append(i)
                else:
                    temp2.append(i)
            for i in v[len(v) - y:]:
                if i >= 0:
                    temp1.append(i)
                else:
                    temp2.append(i)
        temp2.sort()
        ans = max(ans, sum(temp1) + sum(temp2[k - x - y:]))
print(ans)
