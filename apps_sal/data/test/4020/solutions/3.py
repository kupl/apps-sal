s = input()
s1 = input()

h = int(s[:2])
m = int(s[3:])
t = h * 60 + m
h = int(s1[:2])
m = int(s1[3:])
t2 = h * 60 + m

t = (t2 + t) // 2
h = t // 60
m = t % 60
print(h // 10, h % 10, ':', m // 10, m % 10, sep="")
