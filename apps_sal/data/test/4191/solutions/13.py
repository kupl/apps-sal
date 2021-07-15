a = int(input())
b = int(input())
c = int(input())
d = int(input())

# res = ((a or b) and (c ^ d)) or ((b and c) ^ (a or d))
res = ((a ^ b) and (c or d)) ^ ((b and c) or (a ^ d))

print(1 if res else 0)
