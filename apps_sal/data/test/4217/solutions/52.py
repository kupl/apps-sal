n, m = map(int, input().split())
data = [0] * n
for i in range(n):
    data[i] = input().split()
ans = 0
if n == 1:
    print(len(data[0]) - 1)
else:
    for i in range(1, int(data[0][0]) + 1):
        bool = True
        for j in range(1, n):
            if data[0][i] not in data[j][1:]:
                bool = False
        if bool:
            ans += 1
    print(ans)
