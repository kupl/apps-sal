import re
temp = input()
temp = re.split(' ', temp)
n = eval(temp[0])
m = eval(temp[1])
temp = input()
temp = re.split(' ', temp)
a = []
for i in range(n):
    a.append(eval(temp[i]))
i = 0
temp = input()
temp = re.split(' ', temp)
for j in range(m):
    x = eval(temp[j])
    if i >= n:
        continue
    if x >= a[i]:
        i += 1
ans = n - i
print(ans)
