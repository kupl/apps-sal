N = int(input())
H = list(map(int, input().split()))
cnt = 0
mx = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        cnt += 1
    else:
        i += cnt
        cnt = 0
    if mx < cnt:
        mx = cnt
print(mx)
