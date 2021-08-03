N = int(input())
D = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 1
for i in range(len(D) - 1):
    if D[i] <= D[i + 1]:
        pass
    else:
        cnt += 1
print(cnt)
