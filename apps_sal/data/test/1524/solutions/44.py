s = input()
n = len(s)
R = [] # the number of consecutive 'R's on and toward the left
L = [] # the number of consecutive 'L's on and toward the right
ans = []

cnt = 0
for i in range(n):
    if s[i] == 'R':
        cnt += 1
    else:
        cnt = 0
    R.append(cnt)
R.append(0)

s = s[::-1]
cnt =0
for i in range(n):
    if s[i] == 'L':
        cnt += 1
    else:
        cnt = 0
    L.append(cnt)
L.append(0)

r= [0]*n # the number of children coming from 'R' series and stay there
for i in range(n):
    if R[i] != 0 and R[i+1] ==0:
        if R[i] % 2 == 1:
            r[i] = (R[i] + 1) // 2
            r[i+1] = (R[i] - 1) // 2
        else:
            r[i] = R[i] // 2
            r[i+1] = R[i] // 2

l = [0]*n # the number of children coming from 'L' series and stay there
for i in range(n):
    if L[i] != 0 and L[i+1] ==0:
        if L[i] % 2== 1:
            l[i] = (L[i] + 1) // 2
            l[i+1] = (L[i] - 1) // 2
        else:
            l[i] = L[i] // 2
            l[i+1] = L[i] // 2
l = l[::-1]

for i in range(n):
    ans.append(r[i]+l[i])

for i in range(n-1):
    print(ans[i], end = ' ')
print(ans[n - 1])
