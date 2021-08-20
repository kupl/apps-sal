T = input()
n = len(T)
i = 0
L = []
t = 0
while i < n:
    if int(T[i]) % 3 == 0:
        t += 1
        L = []
    else:
        L.append(int(T[i]) % 3)
        if L == [1, 1, 2] or L == [1, 1, 1] or L == [1, 2] or (L == [2, 1]) or (L == [2, 2, 1]) or (L == [2, 2, 2]):
            L = []
            t += 1
    i += 1
print(t)
