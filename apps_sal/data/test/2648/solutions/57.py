N = int(input())
cnt = [0] * (10 ** 5 + 1)
A = [int(_) for _ in input().split()]
for i in range(N):
    cnt[A[i]] += 1
m = 0
for i in range(10 ** 5 + 1):
    if cnt[i] > 0 and cnt[i] % 2 == 0:
        m += 1
print(len(set(A)) - int(m % 2 == 1))
