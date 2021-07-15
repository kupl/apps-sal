N = int(input())
Dic = dict()
for i in range(N):
    A,B = list(map(int,input().split()))
    if B not in Dic:
        Dic[B] = A
    else:
        Dic[B] += A
Deadlines = sorted(Dic)
Time = 0
for Deadline in Deadlines:
    if Time+Dic[Deadline] <= Deadline:
        Time += Dic[Deadline]
    else:
        Ans = 'No'
try:
    if Ans =='No':
        print(Ans)
except:
    print('Yes')

