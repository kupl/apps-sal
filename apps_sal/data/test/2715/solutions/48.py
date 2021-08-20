K = int(input())
k = K // 50
l = K % 50
ans = [i + k for i in range(51) if i != 50 - l]
print(50)
print(*ans)
