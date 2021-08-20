O = input()
E = input()
t = ''
n = min(len(O), len(E))
for i in range(n):
    t += O[i] + E[i]
if len(O) > len(E):
    t += O[len(O) - 1]
elif len(O) < len(E):
    t += E[len(E) - 1]
print(t)
