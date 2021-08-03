def LI():
    return list(map(int, input().split()))


N = int(input())
H = LI()
ans = 0
count = 0
for i in range(1, N):
    if H[i - 1] >= H[i]:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
print((max(ans, count)))
