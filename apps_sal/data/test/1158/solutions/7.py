(n, k) = map(int, input().split())
lst = list(map(int, input().split()))
a = [0] * 101
cnt = 0
for i in lst:
    a[i] += 1
    if a[i] == 1:
        cnt += 1
x = max(a)
if x % k == 0:
    p = x // k
else:
    p = x // k + 1
print(cnt * p * k - n)
