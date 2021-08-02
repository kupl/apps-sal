S = input()
T = input()
t = 0
s = 0
a = 0
while a <= len(S) - len(T):
    u = S[a:a + len(T)]
    for j in range(len(T)):
        if u[j] == T[j]:
            t = t + 1
    if s < t:
        s = t
    t = 0
    a = a + 1
print(len(T) - s)
