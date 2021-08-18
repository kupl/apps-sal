N = int(input())

A = list(map(int, input().split()))
B = 0
C = 1

if 0 in A:
    print(0)
    return

for i in range(N):
    C = C * A[i]
    if C > 1000000000000000000:
        print(-1)
        return

print(C)
