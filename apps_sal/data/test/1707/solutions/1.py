n = int(input())
A = list(map(int, input().split()))
A = [abs(a) for a in A]
A.sort()
j = 0
ANS = 0
for i in range(n - 1):
    while j < n - 1 and A[j + 1] - A[i] <= A[i]:
        j += 1
    ANS += j - i
print(ANS)
