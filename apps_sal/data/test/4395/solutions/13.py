n = int(input())
s = input()

R = [0,0,0]
G = [0,0,0]
B = [0,0,0]

L = ["RGB", "RBG", "BRG", "BGR", "GBR", "GRB"]

for i in range(n):
    if s[i] == "R":
        R[i%3] += 1
    if s[i] == "G":
        G[i%3] += 1
    if s[i] == "B":
        B[i%3] += 1
    
mi = 10**9
for l in L:
    dif = 0
    for i in range(3):
        if l[i] == "R":
            dif += G[i] + B[i]
        elif l[i] == "G":
            dif += R[i] + B[i]
        else:
            dif += R[i] + G[i]
        
    if dif < mi:
        mi = dif
        tmp = l
        
print(mi)
print((tmp*((n+10)//3))[:n])


