(N, A, B) = list(map(int, input().split()))
count = 0
ans = []
for i in range(1, N + 1):
    cal = []
    for k in str(i):
        cal.append(int(k))
    if A <= sum(cal) <= B:
        ans.append(i)
print(sum(ans))
