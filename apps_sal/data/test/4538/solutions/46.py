N, D = map(int, input().split())
X = [0 for i in range(N)]
Y = [0 for i in range(N)]
for i in range(N):
    X[i], Y[i] = map(int, input().split())
cnt = 0

for i in range(N):
    if D**2 >= (X[i]**2 + Y[i]**2):
        cnt += 1

print(cnt)
