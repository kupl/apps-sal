N = int(input())
s = input()
t = ''
for i in s:
    t += i
    if t.endswith('fox'):
        t = t[:-3]
print(len(t))
