a=list(input())
if a[len(a)-1]=="s":
    a.append("e")
a.append("s")
print(*a, sep="")

