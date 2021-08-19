N = int(input())
tasks = []
for i in range(N):
    (A, B) = [int(x) for x in input().split()]
    tasks.append([B, A])
tasks.sort()
ok = True
S = 0
for i in range(N):
    (B, A) = (tasks[i][0], tasks[i][1])
    S += A
    if S > B:
        ok = False
        break
if ok == True:
    print('Yes')
else:
    print('No')
