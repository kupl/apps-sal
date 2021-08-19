n = int(input())
R = []
for i in range(n):
    a, b = list(map(int, input().split()))
    R.append((a, b))
B = []
for i in range(n):
    c, d = list(map(int, input().split()))
    B.append((c, d))

R.sort(reverse=True)  # aをx座標でソート
B.sort(key=lambda x: x[1])  # bをｙ座標でソート
ans = 0
for i in R:
    for j in range(len(B)):
        if i[0] < B[j][0] and i[1] < B[j][1]:
            ans += 1
            B.pop(j)
            break

print(ans)
