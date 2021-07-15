N = int(input())
S = list(map(int, input().split()))
a=1
for i in range(N):
    if S[i]==a:
        a=a+1
if a==1:
    print(-1)
else:
    print(N-a+1)
