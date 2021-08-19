from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
sum = 0
for (k, v) in list(cnt.items()):
    sum += v * (v - 1) // 2
for i in range(N):
    num = cnt.get(A[i])
    if num == 1:
        ans = sum
    elif num == 2:
        ans = sum - 1
    else:
        ans = sum - num * (num - 1) // 2 + (num - 1) * (num - 2) // 2
    print(ans)
