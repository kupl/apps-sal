s = input()
m = ['A', 'C', 'G', 'T']
ans = 0
t = 0
for i in range(len(s)):
    if s[i] in m:
        t += 1
    else:
        ans = max(ans, t)
        t = 0
print(max(ans, t))
