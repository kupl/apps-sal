K = int(input())
ans = [i for i in range(50)]
cnt = 0
loop = K % 50
plus = K // 50
ans = list(map(lambda x: x + plus, ans))
for i in range(loop):
    cnt %= 50
    ans = list(map(lambda x: x - 1, ans))
    ans[cnt] += 51
    cnt += 1
print(50)
print(*ans)
