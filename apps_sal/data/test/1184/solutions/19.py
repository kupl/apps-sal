inp = input()

res = [0 for i in range(30)]

for c in inp:
    if ord('a') <= ord(c) <= ord('z'):
        res[ord(c) - ord('a')] = 1

print(sum(res))
