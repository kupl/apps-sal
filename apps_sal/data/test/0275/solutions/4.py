from sys import stdin
s = list(stdin.readline().strip()[::-1])
s1 = list(stdin.readline().strip()[::-1])


def trans(s):
    s.append("0")
    i = len(s) - 1
    while i > 1:
        while i >= len(s):
            s.append("0")
        if s[i - 1] == "1" and s[i - 2] == "1":
            s[i] = "1"
            s[i - 1] = "0"
            s[i - 2] = "0"
            i += 2
        else:
            i -= 1
    while len(s) > 0 and s[-1] == "0":
        s.pop()
    return s


s = trans(s)
s1 = trans(s1)
for i in range(min(len(s), len(s1))):
    if s[i] == s1[i]:
        s[i] = "0"
        s1[i] = "0"
while len(s) > 0 and s[-1] == "0":
    s.pop()
while len(s1) > 0 and s1[-1] == "0":
    s1.pop()
if len(s) == len(s1):
    print("=")
elif(len(s) > len(s1)):
    print(">")
else:
    print("<")
