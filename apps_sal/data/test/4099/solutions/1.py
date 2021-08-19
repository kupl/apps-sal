(N, K, M) = map(int, input().split())
A = list(map(int, input().split()))
now_total = 0
target_total = N * M
for i in A:
    now_total += i
target_point = target_total - now_total
if 0 < target_point <= K:
    print(target_point)
elif target_point <= 0:
    print(0)
else:
    print(-1)
