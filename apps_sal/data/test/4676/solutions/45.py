o = list(input())
e = list(input())
for i in range(len(e)):
    print(o[i],end="")
    print(e[i],end="")
if len(o) > len(e):
    print(o[-1])
