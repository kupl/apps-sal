n,m = map(int,input().split())
a = set([int(input()) for _ in range(m)])
step = [0] * (n+1)
step[0] = 1
if 1 not in a:
    step[1] = 1
else:
    step[1] = 0
for i in range(2,n+1):
    if i in a:
        continue
    step[i] = (step[i-1] + step[i-2]) % 1000000007
print(step[-1])
