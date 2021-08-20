ar = [tuple(map(int, input().split(' '))) for i in range(8)]
ar.sort()
print('respectable' if ar[0][0] == ar[1][0] == ar[2][0] and ar[3][0] == ar[4][0] and (ar[5][0] == ar[6][0] == ar[7][0]) and (ar[0][1] == ar[3][1] == ar[5][1]) and (ar[1][1] == ar[6][1]) and (ar[2][1] == ar[4][1] == ar[7][1]) and (ar[0][0] < ar[3][0] < ar[5][0]) and (ar[0][1] < ar[1][1] < ar[2][1]) else 'ugly')
