import sys
n = int(input())
sh = list(input())
m = list(input())
sh.sort()
m.sort()
i = 0
j = 0
ans1 = n
while True:
    if j >= n:
        break
    if(sh[i] > m[j]):
        j += 1
    else:
        ans1 -= 1
        i += 1
        j += 1
ans2 = 0
i = 0
j = 0
while True:
    if j >= n:
        break
    if(sh[i] < m[j]):
        i += 1
        ans2 += 1
        j += 1
    else:
        j += 1
print(ans1)
print(ans2)
