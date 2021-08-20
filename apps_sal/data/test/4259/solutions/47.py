K = int(input())
(A, B) = map(int, input().split())
li = []
for i in range(A, B + 1):
    li.append(i)
ans = False
for j in li:
    if j % K == 0:
        ans = True
        break
    else:
        ans = False
if ans == True:
    print('OK')
else:
    print('NG')
