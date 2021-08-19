(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if str(a[i]).count('4') + str(a[i]).count('7') <= k:
        cnt += 1
print(cnt)
