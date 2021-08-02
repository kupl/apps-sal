n, x = map(int, input().split())
mark = [0 for x in range(1 << 18 + 1)]
mark[x] = 1
curent = 0
maxA = 1 << n
ans = []
for i in range(1, maxA):
    if i != x:
        result = i ^ x
        if mark[i] == 0:
            ans.append(i ^ curent)
            mark[result] = 1
            mark[i] = 1
            curent = i
        elif mark[result] == 0 and result < maxA:
            ans.append(curent ^ result)
            mark[result] = 1
            curent = result
print(len(ans))
print(*ans)
