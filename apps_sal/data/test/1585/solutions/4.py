
X, Y = map(int, input().split())
cnt = 0
i = X
while i <= Y:
    cnt += 1
    i = i * 2
print(cnt)
