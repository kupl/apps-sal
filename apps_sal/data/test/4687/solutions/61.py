# 95 C - Big Array
N, K = map(int, input().split())
lis = []
for _ in range(N):
    a, b = map(int, input().split())
    lis.append((a, b))

lis = sorted(lis, reverse=False)

cnt = 0
num = 0
for a, b in lis:
    cnt += b
    num = a
    if cnt >= K:
        break
print(num)
