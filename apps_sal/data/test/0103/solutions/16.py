n = int(input())
A = list(map(int, input().split()))
A = [0] + A + [1001]
ANS = 0
count = 0
for i in range(1, n + 1):
    if A[i] == A[i - 1] + 1 and A[i] == A[i + 1] - 1:
        count += 1
    else:
        ANS = max(ANS, count)
        count = 0
ANS = max(ANS, count)
print(ANS)
