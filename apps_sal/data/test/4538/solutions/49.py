N, D = list(map(int, input().split()))
cnt = 0

for i in range(N):
    x, y = list(map(int, input().split()))
    if x**2 + y**2 <= D**2:
        cnt += 1
    else:
        pass

print(cnt)
