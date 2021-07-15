N = int(input())
A = []
B = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    if(i == 0):
        A.append(B[0])
        continue
    if(i == N-1):
        A.append(B[N-2])
        continue
    a = B[i-1]
    b = B[i]
    if(a < b):
        A.append(a)
    else:
        A.append(b)
for i in A:
    ans += i
print(ans)
