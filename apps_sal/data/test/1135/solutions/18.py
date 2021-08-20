n = int(input())
s = input()
sr = ''
nn = n
if n % 2 == 1:
    flag = True
else:
    flag = False
m = 0
while m < n:
    if flag:
        sr = sr + s[m]
    else:
        sr = s[m] + sr
    flag = not flag
    m += 1
print(sr)
