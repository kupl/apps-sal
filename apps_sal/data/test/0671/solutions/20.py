n = int(input())

t = 1
s = ''

while (len(s) < 1000):
    s += str(t)
    t += 1

print(s[n - 1])
