s = input()
t = ['A', 'E', 'I', 'O', 'U' , 'Y']
cur = -1
n = len(s)
m = 0
for i in range(n):
    if s[i] in t:
        m = max(m, i - cur)
        cur = i
m = max(n - cur, m)
print(m)
