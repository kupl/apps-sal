N, A, B = list(map(int, input().split()))
ans = []
for i in range(1, N + 1):
    target = 0
    for j in range(len(str(i))):
        target += int(str(i)[j])
    if A <= target <= B:
        ans.append(i)

print((sum(ans)))

