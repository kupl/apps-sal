N = int(input())
*A, = list(map(int, input().split()))
su = sum(A)
if su * 2 >= 9 * N:
    print(0)
    return

A.sort()
for i in range(N):
    su += 5 - A[i]
    if su * 2 >= 9 * N:
        print(i + 1)
        return
return
