s = input()
t = input()

S = "".join(sorted(list(s)))
T = "".join(sorted(list(t), reverse=True))

if S < T:
    print("Yes")
else:
    print("No")
