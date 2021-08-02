S = input()
A = 0
B = 0
for s in S:
    if s == "a":
        A += 1
    else:
        B += 1

print(min(A * 2 - 1, A + B))
