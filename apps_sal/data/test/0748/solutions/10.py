a = [0 for i in range(8)]
N = int(input())
b = list(map(int, input().split()))
for k in range(N):
    a[b[k - 1]] = a[b[k - 1]] + 1
if a[5] or a[7]:
    print(-1)
    return
A, C = a[4], a[3]
B = a[6] - C
if A >= 0 and B >= 0 and C >= 0 and A + B == a[2] and A + B + C == a[1]:
    for i in range(A):
        print("1 2 4")
    for i in range(B):
        print("1 2 6")
    for i in range(C):
        print("1 3 6")
else:
    print(-1)
