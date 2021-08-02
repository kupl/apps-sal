S = input()
s = set(S)
for c in s:
    if S.count(c) != 2:
        print("No")
        break
else:
    print("Yes")
