s = input()
k = set(list(s))
if len(k) == 1:
    print(0)
elif s == s[::-1]:
    print(len(s) - 1)
else:
    print(len(s))
