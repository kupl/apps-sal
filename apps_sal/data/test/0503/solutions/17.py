n, k = list(map(int, input().split()))
main = list(map(int, input().split()))

freq, kolgeom, kolvo = {}, {}, 0

for a in main:
    if not (a in freq):
        freq[a] = 0
    if a % k == 0:
        if (a / k) in kolgeom:
            kolvo += kolgeom[a / k]
        if not(a in kolgeom):
            kolgeom[a] = 0
        if (a / k) in freq:
            kolgeom[a] += freq[a / k]
    freq[a] += 1
print(kolvo)
