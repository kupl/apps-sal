n = int(input())

li = [0] * 100
for i in range(n + 1):
    li[int(str(i)[0] + str(i)[-1])] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += li[int(str(i) + str(j))] * li[int(str(j) + str(i))]

print(ans)
