n, k = map(int, input().split())
s = list(input())

while k:
    t = s + s
    s = []
    for i in range(n):
        a, b = t[i * 2], t[i * 2 + 1]
        if a == b:
            s.append(a)
        elif (a == "P" and b == "R") or (a == "R" and b == "P"):
            s.append("P")
        elif (a == "P" and b == "S") or (a == "S" and b == "P"):
            s.append("S")
        elif (a == "S" and b == "R") or (a == "R" and b == "S"):
            s.append("R")
    k -= 1
print(s[0])
