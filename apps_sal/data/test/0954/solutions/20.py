s = input()

n = len(s)

i = 0
a = []
while i < 50:
    s = s[-1] + s[:n - 1]
    if s not in a: a.append(s)
    i += 1
print(len(a))
