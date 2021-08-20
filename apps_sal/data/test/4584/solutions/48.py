N = int(input())
A = [0] * 2 + list(map(int, input().split()))
l = [0] * (N + 1)
for i in range(2, N + 1):
    l[A[i]] += 1
for i in range(1, N + 1):
    print(l[i])
