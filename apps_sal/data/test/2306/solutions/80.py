N = int(input())
T = [2 * int(i) for i in input().split()]
V = [2 * int(i) for i in input().split()]

su = sum(T)
A = [min(i, su - i) for i in range(su + 1)]

cnt = 0
for t, v in zip(T, V):
    for i in range(cnt, cnt + t + 1):
        A[i] = min(A[i], v)
    cnt += t

for i in range(su):
    A[i + 1] = min(A[i + 1], A[i] + 1)

for i in reversed(range(su)):
    A[i] = min(A[i], A[i + 1] + 1)

print(sum(A) / 4)
