N = int(input())
A = []
B = []
for i in range(N):
    (x, y) = map(int, input().split())
    a = x + y
    A.append(a)
    b = x - y
    B.append(b)
A.sort()
B.sort()
Max_A = A[-1] - A[0]
Max_B = B[-1] - B[0]
ans = max(Max_A, Max_B)
print(ans)
