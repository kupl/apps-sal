N = input()

o1 = set(N[0:3])
o2 = set(N[1:])
o3 = set(N)


print("Yes" if len(o1) == 1 or len(o2) == 1 or len(o3) == 1 else "No")
