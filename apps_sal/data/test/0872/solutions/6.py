from sys import stdin
n=int(stdin.readline().strip())
s=list(map(int,stdin.readline().strip().split()))
odd=False
even=False
for i in range(n):
    if s[i]%2==0:
        even=True
    else:
        odd=True
if even and odd:
    s.sort()
    print(*s)
else:
    print(*s)

