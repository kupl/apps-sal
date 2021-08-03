n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
sum = 0
for i in A:
    sum += i
A.sort(reverse=True)
if A[m - 1] >= sum / (4 * m):
    print("Yes")
else:
    print("No")
