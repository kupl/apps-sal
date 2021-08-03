from bisect import bisect_left
n = int(input())
S = A = list(map(int, input().split()))
for i in range(1, n):
    S[i] += S[i - 1]
m = int(input())
for q in list(map(int, input().split())):
    print(bisect_left(S, q) + 1)
