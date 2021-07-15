N, M = map(int, input().split())
AC = [0]*(N+1)
WA = [0]*(N+1)

for i in range (0, M):
    A, B = map(str, input().split())
    A = int(A)
    if B == 'WA':
        if AC[A] == 0:
            WA[A]+=1
    else:
        if AC[A] == 0:
            AC[A] = 1

Wronganswer = 0
for i in range (0, N+1):
    Wronganswer+=(AC[i]*WA[i])
print(sum(AC), Wronganswer)
