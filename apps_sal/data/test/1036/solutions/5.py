n, k = list(map(int, input().split()))
s = input()

for _ in range(k):
    tmp = ""
    for i in range(0, 2 * n, 2):
        s1 = s[i % n]
        s2 = s[(i + 1) % n]
        if s1 == s2:
            tmp += s1
        elif (s1, s2) in (("R", "S"), ("S", "R")):
            tmp += "R"
        elif (s1, s2) in (("P", "S"), ("S", "P")):
            tmp += "S"
        else:
            tmp += "P"
            
    s = tmp
print((s[0]))

