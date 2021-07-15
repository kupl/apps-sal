N = int(input())
s = input()

t = ''
for i in range(N):
    t += s[i]
    if t.endswith('fox'):
        t = t[:-3]
print(len(t))
