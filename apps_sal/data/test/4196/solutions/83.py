from math import gcd

N = int(input())
A = list(map(int, input().split()))

L = [0]
for i in range(N):
    L.append(gcd(L[-1], A[i]))


R = [0]
for i in range(N):
    R.append(gcd(R[-1], A[-i - 1]))
R = R[::-1]

ans_list = []
for i in range(N):
    ans_list.append(gcd(L[i], R[i + 1]))

print((max(ans_list)))
