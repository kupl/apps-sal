input()
horiz = input()
vert = input()

m = horiz[0] + horiz[-1] + vert[0] + vert[-1]

print("YES" if m in ("><^v", "<>v^") else "NO")
