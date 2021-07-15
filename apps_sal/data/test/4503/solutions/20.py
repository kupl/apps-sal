H, N = map(int, input().split())
A = list(map(int, input().split()))

AA = sum(A)

if AA >= H:
    print("Yes")
else:
    print("No")
