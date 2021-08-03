import math

N = int(input())
A = list(map(int, input().split()))
gcd1 = [A[0]]
gcd2 = [A[N - 1]]
ans_list = []

for i in range(1, N - 1):
    gcd1.append(math.gcd(gcd1[-1], A[i]))
    gcd2.append(math.gcd(gcd2[-1], A[N - i - 1]))

ans_list.append(gcd1[-1])
for j in range(N - 2):
    ans_list.append(math.gcd(gcd1[j], gcd2[N - j - 3]))
ans_list.append(gcd2[-1])

print(max(ans_list))
