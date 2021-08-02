
N, M = map(int, input().split())

l = []
for _ in range(N):
    l.append(list(map(int, input().split())))

sorted_l = sorted(l, key=lambda x: x[0])

ans = 0
count = 0
flag = 0
for i in sorted_l:
    if flag == 1:
        break
    for j in range(i[1]):
        if count >= M:
            flag = 1
            break
        ans += i[0]
        count += 1
print(ans)
