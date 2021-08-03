S = input()
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in S:
        print(c)
        break
else:
    print("None")
