N = int(input())
A = list(map(int, input().split()))
cnt = [0 for _ in range(100001)]
for i in range(N):
    cnt[A[i]] = 1
x = cnt.count(1)
y = N - x
if y % 2 == 0:
    print(N - y)
else:
    print(N - y - 1)
