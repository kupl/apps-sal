n, M = map(int, input().split())
t = list(map(int, input().split()))
ans = []
for i in range(n):
    num = 0
    tmp = []
    T = 0
    for j in range(n):
        if i != j:
            tmp.append(t[j])
        else:
            T += t[i]
            break

    tmp = sorted(tmp)
    for j in range(len(tmp)):
        if T + tmp[j] <= M:
            T += tmp[j]
            num += 1

    ans.append(len(tmp) - num)

print(*ans)
