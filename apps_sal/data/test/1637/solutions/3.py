import sys

n,m = [int(x) for x in input().split()]

s = sys.stdin.read()

inp = []
numb = 0
sign = 1
 
for i in range(len(s)):
    if s[i]>='0':
        numb = 10*numb + ord(s[i])-48
    else:
        if s[i]=='-':
            sign = -1
        else:
            inp.append(sign*numb)
            numb = 0
            sign = 1
if s[-1]>='0':
    inp.append(sign*numb)

order = sorted(range(n),key=lambda i:inp[2*i]-inp[2*i+1])

score = [0]*n
val = sum(inp[1:2*n:2])
for ind in range(n):
    i = order[ind]

    # Do second problem together with order[:ind]
    # Do first problem together with order[ind:]
    score[i] += val + inp[2*i+1]*(ind-1) + inp[2*i]*(n-ind-1)
    val += inp[2*i]-inp[2*i+1]

for _ in range(m):
    u = inp[2*n+2*_]-1
    v = inp[2*n+2*_+1]-1
    s = min(inp[2*u]+inp[2*v+1],inp[2*v]+inp[2*u+1])
    score[u] -= s
    score[v] -= s

sys.stdout.write(' '.join(str(x) for x in score))
