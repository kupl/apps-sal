n = int(input())
s = input()
match = []
for i in range(1,len(s)):
    s1 = list(s[:i])
    s2 = list(s[i:])
    cnts = []
    for j in s1:
        if j in s2:
            if j not in cnts:
                cnts.append(j)
    match.append(len(cnts))
print(max(match))
