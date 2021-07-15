n = int(input())

s = input()

lst = []
k = 0
for x in range(n):
    if s[x] == 'x':
        k += 1
    else:
        if k != 0:
            lst.append(k)
        k = 0
if k != 0:
    lst.append(k)
     
ans = 0
for x in lst:
    if x >= 3:
        ans += x - 2

print(ans)

