n,l = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans1 = [0] * n
ans2 = [0] * n
for j in range(n):
    if j == 0:
        
        ans1[j] = A[j] + (l - A[-1-j])
        ans2[j] = B[j] + (l - B[-1-j])
    else:
        ans1[j] = A[j] - A[j-1]
        ans2[j] = B[j] - B[j-1]
per = 0
for j in range(n):
    if ans1 == ans2:
        per = 1
        break
    else:
        s = ans1[0]
        ans1 = ans1[1:]
        ans1.append(s)
if per == 1:
    print('YES')
else:
    print('NO')
