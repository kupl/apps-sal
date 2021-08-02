S = input()
T = input()
ans = [1 for s, t in zip(S, T) if s == t]
print(sum(ans))
