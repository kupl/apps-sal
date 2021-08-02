from collections import Counter
n, k, q = map(int, input().split())
if k > q:
    [print("Yes") for i in range(n)]
    return

a = [int(input()) for i in range(q)]
A = Counter(a)

ans = ['No'] * n
for i in A:
    if k - q + A[i] > 0:
        ans[i - 1] = 'Yes'

for i in ans:
    print(i)
