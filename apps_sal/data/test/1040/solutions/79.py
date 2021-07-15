N = int(input())
s = input()

t = ''
for i in range(N):
    t += s[i]
    if t[-3:] == 'fox':
        t = t[:-3]
print(len(t))
