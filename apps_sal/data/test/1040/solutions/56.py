N = int(input())
s = input()
t = []
for i in range(N):
    t.append(s[i])
    if len(t) >= 3 and t[-3:] == ['f', 'o', 'x']:
        t.pop()
        t.pop()
        t.pop()
print(len(t))
