N = int(input())
A = [int(c) for c in input().split()]

l = [0] * N
for i in range(N):
    l[A[i] - 1] = i + 1

print((' '.join(map(str, l))))
