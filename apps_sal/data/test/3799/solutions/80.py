from operator import xor
S = input()
a = (len(S) + 1) % 2
b = int(S[0] == S[-1])
ans = 'Second' if xor(a, b) else 'First'
print(ans)
