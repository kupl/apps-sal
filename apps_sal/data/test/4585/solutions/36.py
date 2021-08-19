X = int(input())
cnt = 0
s = 0
for i in range(1, X + 1):
    cnt += 1
    s += i
    if s >= X:
        break
print(cnt)
