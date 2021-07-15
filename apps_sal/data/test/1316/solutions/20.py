n, k = [ int(a) for a in input().split() ]
s = input()

freq = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
    freq[c] = 0

prev = '!'
run = 0
for x in s:
    if x == prev:
        run += 1
    else:
        prev = x
        run = 1

    if run == k:
        freq[x] += 1
        run = 0

print(max(freq.values()))


