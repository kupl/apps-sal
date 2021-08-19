n = int(input())
A = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    A.append((a, b))
k = int(input())
for i in range(n):
    if k >= A[i][0] and k <= A[i][1]:
        print(n - i)
        break
