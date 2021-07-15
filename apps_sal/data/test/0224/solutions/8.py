s = input()
a = 'AOUYEI'
s += 'A'
ans = -1
now = -1
n = len(s)
for i in range(0, n):
    if s[i] in a:
        #print(i)
        ans = max(ans, i - now)
        now = i
print(ans)
