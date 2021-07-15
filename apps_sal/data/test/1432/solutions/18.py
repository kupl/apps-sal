N = int(input())
A = list(map(int,input().split()))

All = sum(A)

lim = len(A)//2
Exc1 = sum([A[2*i+1] for i in range(lim)])

one = All - Exc1*2
ans = [one]
for i in range(1,N):
    print('{}'.format(ans[-1]),end=' ')
    ans.append(A[i-1]*2 - ans[-1])
print('{}'.format(ans[-1]))

