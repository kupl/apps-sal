n,m = list(map(int, input().split()))
s = input()
t = input()


tot = 1000000000
pos = []

for k in range(m-n+1):
    ctot = 0
    cpos = []

    for e in range(n):
        if s[e] != t[e+k]:
            cpos.append(e+1)
            ctot+=1

    if ctot < tot:
        pos = cpos
        tot = ctot

print(tot)
print(*pos)

