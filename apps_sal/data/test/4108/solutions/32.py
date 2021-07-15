import collections

S = input()
T = input()

S_c = sorted(list(collections.Counter(S).values()))
T_c = sorted(list(collections.Counter(T).values()))

print("Yes" if S_c == T_c else "No")
