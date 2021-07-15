s = list(input())
t = list(input())
A = 10000
for i in range(len(s) - len(t) +1):
    u = s[i : i+len(t)]
    a = 0
    for j in range(len(t)):
        if u[j] != t[j]:
            a += 1
    A = min(A,a)
print(A)
