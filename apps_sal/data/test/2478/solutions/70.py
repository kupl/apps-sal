N = int(input())
S = input()
l = r = 0
L = ""
for i in S:
    if i == "(":
        l += 1
    else:
        r += 1
    if l < r:
        L += "("
        l += 1
R = ")" * (l - r)
print(L + S + R)
