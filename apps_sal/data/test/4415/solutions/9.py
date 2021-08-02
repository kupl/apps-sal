N = int(input())
A = sorted([int(a) for a in input().split()])

pre = -1
c = 0
I = []
D = []
for i in range(N):
    if A[i] == pre:
        c += 1
        if c > 2:
            print("NO")
            break
        D.append(A[i])
    else:
        I.append(A[i])
        pre = A[i]
        c = 1
else:
    print("YES")
    print(len(I))
    print(*I)
    print(len(D))
    print(*sorted(D)[::-1])
