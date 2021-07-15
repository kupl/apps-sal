S = input()

s = [i for i in S]
ss = []

i = 0
while i < len(s) - 2:
    ss.append(abs(753 - int("".join(s[i:i+3]))))
    i += 1

print(min(ss))
