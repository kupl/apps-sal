from sys import stdin
n=int(stdin.readline().strip())

s=list(map(int,stdin.readline().strip().split()))
s.sort()
if sum(s[0:n])!=sum(s[n:2*n]):
    print(*s)
else:
    print(-1)

