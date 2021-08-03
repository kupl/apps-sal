import collections
S = input()
T = input()
if sorted(collections.Counter(S).values()) == sorted(collections.Counter(T).values()):
    print("Yes")
else:
    print("No")
