n = int(input())
A = list(map(int, input().split()))
A.sort()
i = 0
j = 0
ANS = 0
while j < n:
    while j < n - 1 and A[j + 1] - A[i] <= 5:
        j += 1
    ANS = max(ANS, j - i + 1)
    i += 1
    j = max(j, i)
print(ANS)
