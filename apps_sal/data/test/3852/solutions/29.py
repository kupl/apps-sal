N = int(input())
A = list(map(int, input().split()))
Amax = max(A)
Amin = min(A)

print(N*2)
if abs(Amax) > abs(Amin):
    Amaxi = A.index(Amax)+1
    print(Amaxi, 1)
    print(Amaxi, 1)
    for i in range(1, N):
        print(i, i+1)
        print(i, i+1)

else:
    Amini = A.index(Amin)+1
    print(Amini, N)
    print(Amini, N)
    for i in range(N, 1, -1):
        print(i, i-1)
        print(i, i-1)
