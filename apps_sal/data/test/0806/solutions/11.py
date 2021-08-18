

stuff = list(map(int, input().rstrip().split()))


n = stuff[0]
l = stuff[1]
r = stuff[2]

mod = 10**9 + 7


zeromods = r // 3 - (l - 1) // 3

onemods = (r - 1) // 3 - (l - 2) // 3

twomods = (r - 2) // 3 - (l - 3) // 3


combos = [[0, 0, 0] for i in range(n)]


combos[0] = [zeromods, onemods, twomods]


for i in range(1, n):
    combos[i][0] = (combos[i - 1][0] * zeromods + combos[i - 1][1] * twomods + combos[i - 1][2] * onemods) % mod

    combos[i][1] = (combos[i - 1][0] * onemods + combos[i - 1][1] * zeromods + combos[i - 1][2] * twomods) % mod

    combos[i][2] = (combos[i - 1][0] * twomods + combos[i - 1][1] * onemods + combos[i - 1][2] * zeromods) % mod


print(combos[-1][0])


combos
