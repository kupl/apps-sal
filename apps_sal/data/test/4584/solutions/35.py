import collections
N = int(input())
a = list(map(int, input().split()))
l = [0] * N
for i in range(N - 1):
    l[a[i] - 1] += 1
for j in range(N):
    print(l[j])
