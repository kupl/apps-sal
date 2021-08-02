N = int(input())
*A, = map(int, input().split())

B = [0] + A + [0]
count = [0] * N
S = abs(B[1] - 0)
i = 1
while i <= N:
    if B[i - 1] <= B[i] <= B[i + 1] or B[i - 1] >= B[i] >= B[i + 1]:
        count[i - 1] = 0
    else:
        count[i - 1] = 2 * min(abs(B[i] - B[i - 1]), abs(B[i + 1] - B[i]))
    S += abs(B[i + 1] - B[i])
    i += 1

for c in count:
    print(S - c)
