n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = A[0]
ans2 = B[0]
for i in range(1, n):
    ans1 = ans1 | A[i]
    ans2 = ans2 | B[i]
print(ans1 + ans2)
