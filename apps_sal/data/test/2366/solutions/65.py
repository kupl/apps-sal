N = int(input())
A = list(map(int, input().split()))
S = [0] * (N + 1)
total = 0
for i in A:
    S[i] = S[i] + 1
for i in S:
    total = i * (i - 1) // 2 + total
for i in A:
    a = total - S[i] + 1
    print(a)
