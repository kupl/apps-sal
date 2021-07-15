# ABC110
# A Maximize the Fomula
Num = list(map(int, input().split()))
Num = sorted(Num, reverse=True)
X = []
for i in range(2):
    X.append(str(Num[i]))
X = int("".join(X))
Y = int(Num[2])
print((X + Y))

