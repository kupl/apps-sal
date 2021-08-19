t = [tuple(map(int, input().split())) for i in range(8)]
t.sort()
s = t[0][0] < t[3][0] < t[5][0] and t[0][1] < t[1][1] < t[2][1] and (t[0][0] == t[1][0] == t[2][0]) and (t[3][0] == t[4][0]) and (t[5][0] == t[6][0] == t[7][0]) and (t[0][1] == t[3][1] == t[5][1]) and (t[1][1] == t[6][1]) and (t[2][1] == t[4][1] == t[7][1])
print(['ugly', 'respectable'][s])
