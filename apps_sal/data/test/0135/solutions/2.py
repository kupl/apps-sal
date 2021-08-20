(n, k) = input().split()
(n, k) = (int(n), int(k))
ans = True
n += 1
for i in range(1, min(100, k + 1)):
    if n % i != 0:
        ans = False
if ans:
    print('Yes')
else:
    print('No')
