import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

count = [0] * 50

for i in range(N):
    a = A[i]
    j = 0
    while a:
        if a % 2 == 1:
            count[j] += 1
        j += 1
        a //= 2

B = [0] * 60
k = K
j = 0
while k:
    if k % 2 == 1:
        B[j] = 1
    j += 1
    k //= 2

under = [-1] * (j + 1)
just = [0] * (j + 1)
# print (j)

tmp = 0
for i in range(49, j - 1, -1):
    tmp += pow(2, i) * count[i]

for i in range(j - 1, -1, -1):
    tmp1 = count[i]  # 1の数
    tmp0 = N - tmp1  # 0の数
    if B[i] == 0:
        just[i] = just[i + 1] + pow(2, i) * tmp1
        if under[i + 1] >= 0:
            under[i] = under[i + 1] + pow(2, i) * max(tmp1, tmp0)
    else:  # B[i] == 1
        just[i] = just[i + 1] + pow(2, i) * tmp0
        if under[i + 1] == -1:
            under[i] = just[i + 1] + pow(2, i) * tmp1
        if under[i + 1] >= 0:
            under[i] = under[i + 1] + pow(2, i) * max(tmp1, tmp0)
            under[i] = max(under[i], just[i + 1] + pow(2, i) * tmp1)


print((max(under[0], just[0]) + tmp))

# print ('count', count)
# print ('B', B)
# print (under)
# print (just)
# print (tmp)
