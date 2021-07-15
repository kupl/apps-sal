K = int(input())
k = K // 50
d = K % 50
ans = [k+i for i in range(50)]


for i in range(49, 49-d, -1):
    ans[i] += 1
print(50)
print(*ans)
