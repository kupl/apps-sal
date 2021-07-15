N, X = list(map(int, input().split()))
L = list(map(int, input().split()))

current = 0
cnt = 1
for l in L:
    current += l
    if current > X:
        break
    cnt += 1

print(cnt)

