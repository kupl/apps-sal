n = int(input())
A = list(map(int,input().split()))
L = []
L.append(A[n-1])
cnt = 0
for i in range(n):
    r = A[n-i-1] + A[n-i-2]
    cnt+=1
    if cnt == n:
        break
    # print(r)
    L.append(r)
L.reverse()

print(*L)
