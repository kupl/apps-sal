s = input()
B = s.count("B")
u = s.count("u") // 2
l = s.count("l")
b = s.count("b")
a = s.count("a") // 2
s1 = s.count("s")
r = s.count("r")
print(min(B, u, l, b, a, s1, r))
