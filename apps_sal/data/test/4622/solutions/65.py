N = int(input())
A = sorted(list(map(int,input().split())))

for i in range(1,N):
    if A[i] == A[i-1]:
        print("NO")
        Flag = False
        break
    else:
        Flag = True

if Flag:
    print("YES")
