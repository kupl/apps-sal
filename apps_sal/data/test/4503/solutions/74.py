H, N = map(int, input().split())
A = [int(x) for x in input().split()]

for i in range(N):
    H = H - A[i]

if H > 0:
    print("No")
else:
    print("Yes")
