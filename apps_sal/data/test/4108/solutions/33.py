import collections
S = list(input())
T = list(input())
if sorted(collections.Counter(S).values()) == sorted(collections.Counter(T).values()):
    print("Yes")
else:
    print("No")
