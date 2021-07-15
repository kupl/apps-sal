#   Transfer

a, b, c = list(map(int, input().split()))

residue = c - (a - b)
if residue<0:
    residue=0

print(residue)


