S = input()
b = 1
B = 0
for i in S:
    if int(i) != b:
        B += 1
    b = 1 - b
l = len(S)
print(min(B, l - B))
