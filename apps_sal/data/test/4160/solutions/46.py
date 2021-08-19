X = input()
X = int(X)
M = 100
cnt = 0
while M < X:
    M = M + M // 100
    cnt += 1
print(cnt)
