s1 = input()
s2 = input()

if len(s1) != len(s2):
    print(max(len(s1), len(s2)))
elif s1 == s2:
    print(-1)
else:
    print(len(s1))
