N = str(input())
lenN = len(N)

fN = N[0:(lenN - 1) // 2]
lN = N[(lenN + 3) // 2 - 1:]
print((("No", "Yes")[(0, 1)[fN == fN[-1::-1]] * (0, 1)[lN == lN[-1::-1]] * (0, 1)[lN == fN]]))
