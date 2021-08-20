(n, k) = map(int, input().split())
L = [1] * n
for i in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        L[a - 1] = 0
print(sum(L))
