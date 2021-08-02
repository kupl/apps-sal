S = input()
T = input()
U = [[i, j] for i, j in zip(S, T)]
U.sort()
s = U[0][0]
t = U[0][1]
for i, j in U:
    if i != s:
        s = i
        t = j
    elif j != t:
        print("No")
        return
U.sort(key=lambda x: x[1])
s = U[0][0]
t = U[0][1]
for i, j in U:
    if j != t:
        s = i
        t = j
    elif i != s:
        print("No")
        return
print("Yes")
