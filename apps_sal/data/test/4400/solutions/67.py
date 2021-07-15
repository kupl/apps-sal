s = input()
a0 = ["SSS"]
a1 = ["RSS", "SRS", "SSR", "RSR"]
a2 = ["RRS", "SRR"]
a3 = ["RRR"]
if s in a0:
    ans = 0
elif s in a1:
    ans = 1
elif s in a2:
    ans = 2
else:
    ans = 3
print(ans)
