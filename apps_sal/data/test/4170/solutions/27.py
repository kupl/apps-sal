N = int(input())
H = list(map(int, input().split()))
ans = []
cnt = 0
for i in range(N - 1):
    if H[i] < H[i + 1]:
        ans.append(cnt)
        cnt = 0
    else:
        cnt += 1
ans.append(cnt)
print(max(ans))
