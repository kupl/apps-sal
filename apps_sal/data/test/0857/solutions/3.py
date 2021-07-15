input()
x = [int(a) for a in input().split()]
y = [int(a) for a in input().split()]

z = [str(i) for i in x if i in y]

print(" ".join(z))

