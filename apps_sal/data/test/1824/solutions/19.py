a = int(input())
f = list(map(int, input().split()))
s = list(map(int, input().split()))
t = list(map(int, input().split()))
f.sort()
s.sort()
t.sort()
flag = 0
for i in range(len(s)):
    if f[i] != s[i]:
        flag = 1
        x = f[i]
        break
if flag == 0:
    x = f[-1]
flag = 0
print(x)
for i in range(len(t)):
    if s[i] != t[i]:
        flag = 1
        x = s[i]
        break
if flag == 0:
    x = s[-1]
print(x)
