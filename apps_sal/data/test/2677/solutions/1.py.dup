# cook your dish here
s = input()
l = ["A", "E", "I", "O", "U"]
c = 0
p = 0
if len(s) >= 8:
    for m in range(0, len(s)):
        if s[m] in l:
            if s[m + 1] in l and s[m + 2] in l:
                p = 1
        elif s[m] not in l:
            c += 1
    if c >= 5 and p == 1:
        print("GOOD")
    else:
        print("-1")
