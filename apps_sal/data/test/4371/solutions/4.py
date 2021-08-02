S = input()
x = len(S)
y = []
for n in range(x):
    y.append(abs(753 - int(S[n:n + 3])))
y.sort()
print(y[0])
