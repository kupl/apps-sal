S = input()
T = "abcdefghijklmnopqrstuvwxyz"

for c in T:
    if S.count(c) == 0:
        print(c)
        break
else:
    print("None")
