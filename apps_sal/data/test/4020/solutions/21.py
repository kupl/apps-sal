s1 = input()
s2 = input()
h1, h2, m1, m2 = int(s1[:2]), int(s2[:2]), int(s1[3:]), int(s2[3:])
v1 = h1 * 60 + m1
v2 = h2 * 60 + m2
s = (v1 + v2) // 2
print("0" * (2 - len(str(s // 60))) + str(s // 60) + ":" + "0" * (2 - len(str(s % 60))) + str(s % 60))
