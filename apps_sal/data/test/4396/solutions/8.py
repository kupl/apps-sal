N = int(input())
ans = 0
for _ in range(N):
    xu = input().split()
    if xu[1] == 'JPY':
        ans += int(xu[0])
    else:
        ans += float(xu[0]) * 380000
print(ans + 1e-06)
