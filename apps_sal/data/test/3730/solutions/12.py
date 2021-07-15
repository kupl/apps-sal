from sys import stdin, stdout
n = int(stdin.readline())
a = [int(s) for s in stdin.readline().split()]
left = [0 for i in range(n)]
right = [0 for i in range(n)]

left[0] = 1
for i in range(1, n):
    if a[i] > a[i-1]:
        left[i] = left[i-1] + 1
    else:
        left[i] = 1

right[n-1] = 1
for i in range(n-2,-1,-1):
    if a[i] < a[i+1]:
        right[i] = right[i+1] + 1
    else:
        right[i] = 1

ans = 0

for i in range(1,n-1):
    if a[i+1]-a[i-1]>1:
        ans = max(ans, left[i-1]+1+right[i+1])
    else:
        ans = max(ans, left[i-1]+1, right[i+1]+1)
if n > 1:
    ans = max(ans, 1 + right[1], 1 + left[n-2])
else:
    ans = 1
stdout.write(str(ans))

