l = []
r = []
n = int(input())
for i in range(n):
    s = input().split(' ')
    l.append(int(s[0]))
    r.append(int(s[1]))
k = int(input())
rem = n
i = 0
for i in range(n):
    if l[i] <= k <= r[i]:
        break
    rem -= 1
print(rem)
