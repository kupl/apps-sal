from itertools import chain
data = input()
MOD = 10 ** 9 + 7
translate = [chr(x) for x in chain(list(range(ord('0'), ord('9') + 1)), list(range(ord('A'), ord('Z') + 1)), list(range(ord('a'), ord('z') + 1)), [ord('-'), ord('_')])]
assert len(translate) == 64
translate2 = {k: '{:0>6}'.format(bin(i)[2:]).count('0') for (i, k) in enumerate(translate)}
x = sum([translate2[ch] for ch in data])
print(3 ** x % MOD)
