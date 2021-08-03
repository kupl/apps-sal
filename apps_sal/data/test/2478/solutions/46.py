n = int(input())
s = input()

l = 0
r = 0
p = []
for i in range(n):
    if s[i] == "(":
        p.append("(")
    else:
        if p == []:
            l += 1
        else:
            p.pop()
r = p.count("(")
print("(" * l + s + ")" * r)
