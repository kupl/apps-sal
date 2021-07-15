o=input()
e=input()
p=""
for i in range(len(e)):
    p+=o[i]
    p+=e[i]
if len(o)!=len(e):
    p+=o[-1]
print(p)



