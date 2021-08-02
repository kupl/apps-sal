S = input()
b = 1
B = 0
for i in S:
    if int(i) != int(b):
        B += 1
    b = not b
l = len(S)
print(min(B, l - B))
