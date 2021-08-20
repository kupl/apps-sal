(n, s) = map(int, input().split())
sp = list(map(int, input().split()))
k = 1
for i in range(1, n):
    if sp[i] - sp[i - 1] <= s:
        k += 1
    else:
        k = 1
print(k)
