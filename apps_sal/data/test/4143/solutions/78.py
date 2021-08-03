N = int(input())
A = [int(input()) for i in range(5)]  # A[i]:amount of people able to be carried at once from i to i+1
B = [0] * 6  # B[i]:amount of people at i now
cnt = 0

# max people able to be transported in m minutes
P = [0] * 9
B[0] = 10**15
for m in range(9):
    for i in range(5, 0, -1):
        B[i] += min(A[i - 1], B[i - 1])
        B[i - 1] -= min(A[i - 1], B[i - 1])

    P[m] = B[5]
    cnt += 1
# print(P)
x = N // P[-1]
y = N % P[-1]
if y == 0:
    print((5 * x + 4))
    return
for j in range(7, 2, -1):
    if P[j] < y:
        time = 5 * x + j + 2
        print(time)
        return
