_ = input()
s1 = list(input())
s2 = []

for c in s1:
    try:
        if c == "x" and s2[-1] == "o" and s2[-2] == "f":
            s2.pop()
            s2.pop()
        else:
            s2.append(c)
    except:
        s2.append(c)
    

print((len(s2)))

