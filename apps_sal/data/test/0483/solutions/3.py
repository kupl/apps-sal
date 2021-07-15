n = int(input())
a = input()
answer = float('infinity')
A = list(map(int, input().split()))
for i in range(n-1):
    if a[i]=='R' and a[i+1] == 'L':
        answer = min(answer, (A[i+1] - A[i])//2)
if answer != float('infinity'):
    print(answer)
else:
    print(-1)
