N = int(input())
S = input()
nS = S
for i in range(50):
    nS = nS.replace("()", "")
r = nS.count(")")
l = nS.count("(")
print("(" * r + S + ")" * l)
