(*S,) = input()
n = sum([1 for s in S if s == '+'])
print(n - (len(S) - n))
