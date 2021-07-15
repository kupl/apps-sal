L = [list(map(int, input().split())) for _ in range(3)]
T = sum([sum(i) for i in L])
print('Yes' if L[0][0] + L[1][1] + L[2][2] == (T / 3) else 'No')
