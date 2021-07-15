a = []
n = int(input())
a = input().strip()
cnt = 0
l = -1
r = -1
for i in range(n):
    if a[i] == '.':
        if l == -1 and r == -1:
            cnt += 1
    if a[i] == 'L':
        if r != -1:
            l = i
            cnt += (l - r + 1) % 2
        else:
            cnt -= i
            l = i
    if a[i] == 'R':
        if l != -1:
            r = i
            cnt += r - l - 1
        else:
            r = i
if l > r:
    cnt += n - l - 1
print(cnt)
            
        

