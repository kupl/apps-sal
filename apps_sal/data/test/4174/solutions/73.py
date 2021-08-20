(N, X) = list(map(int, input().split()))
L = list(map(int, input().split()))
cnt = 1
total = 0
for i in range(N):
    total += L[i]
    if total <= X:
        cnt += 1
    else:
        break
print(cnt)
