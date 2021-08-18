import sys
n = int(input())
l = [int(i) for i in input().split()]
l += [l[0]]
jump = False
j = -1
m = l[0]
for i in range(n):
    if l[i] > l[i + 1]:
        if jump:
            print(-1)
            return
        jump = True
        j = i
    else:
        if jump:
            if l[i] > m:
                print(-1)
                return

if j == -1:
    print(0)
else:
    print(n - j - 1)
