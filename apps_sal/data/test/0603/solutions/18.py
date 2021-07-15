#190 div 2 B. Ciel and Flowers

data = input().split(" ")
r = int(data[0])
g = int(data[1])
b = int(data[2])
r2 = False
g2 = False
b2 = False

bonquets = 0
if r%3 == 2:
	r2 = True
if g%3 == 2:
	g2 = True
if b%3 == 2:
	b2 = True

if (r2 and g2) or (r2 and b2) or (g2 and b2):
	if min(r,g,b) >= 2:
		r -= 2
		g -= 2
		b -= 2
		bonquets += 2

bonquets += int(r/3)
r = r%3
bonquets += int(g/3)
g = g%3
bonquets += int(b/3)
b = b%3

bonquets += min(r, g, b)

print(bonquets)
