import sys
s = input()
s1 = input()
ans = 0
x = [0] * 27
y = [0] * 27
for i in range(len(s)):
    x[ord(s[i]) - 97]+=1
for i in range(len(s1)):
    y[ord(s1[i]) - 97] += 1
for i in range(27):
    if x[i] == 0 and y[i] != 0:
        print(-1)
        return
    ans += min(x[i], y[i])
print(ans)
