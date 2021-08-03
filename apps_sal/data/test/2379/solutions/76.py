N, K, C = list(map(int, input().split()))
S = input().strip("\n")

L = [-1] * N
R = [10 ** 10] * N

l = 1
r = K
li = 0
ri = N - 1
while li < N:
    if S[li] == "o":
        L[li] = l
        l += 1
        li += C + 1
    else:
        li += 1

while ri >= 0:
    if S[ri] == "o":
        R[ri] = r
        r -= 1
        ri -= C + 1
    else:
        ri -= 1


for i in range(N):
    if L[i] == R[i]:
        print((i + 1))
