n = int(input())
a = list(map(int, input().split()))
k = 0
fails = 0
ans = []
for i in range(n):
    if a[i] < 0 and fails == 2:
        ans.append(k)
        k = 1
        fails = 1
    else:
        k += 1
        fails += a[i] < 0
if sum(ans) < n:
    ans.append(k)
print(len(ans))
print(' '.join(map(str, ans)))
