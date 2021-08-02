s = input()

g = s.count("g")
p = s.count("p")

max_p = (g + p) // 2
max_g = g + p - (g + p) // 2

print(max_p - (max_g - (g - max_p)))
