(n, k) = list(map(int, input().split()))
d = [0] * k
A = []
for i in range(k):
    d = int(input())
    A += list(map(int, input().split()))
    list(set(A))
cnt = 0
for i in range(n):
    if i + 1 not in A:
        cnt += 1
print(cnt)
