N = int(input())
A = list(map(int, input().split()))
AA = 1

if 0 in A:
    print(0)
    return

for i in range(N):
    AA *= A[i]
    if AA > 10**18:
        print(-1)
        return

print(AA)
