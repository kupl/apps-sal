s = input()
d = [[0 for i in range(len(s) + 5)] for j in range(3)]
for i in range(1, len(s) + 1):
    d[0][i] = d[0][i - 1] + (s[i - 1] == 'b')
    d[1][i] = d[1][i - 1] + (s[i - 1] == 'a')
    d[1][i] = min(d[1][i], d[0][i - 1] + (s[i - 1] == 'a'))
    d[2][i] = d[2][i - 1] + (s[i - 1] == 'b')
    d[2][i] = min(d[2][i], d[1][i - 1] + (s[i - 1] == 'b'))
n = len(s)
print(len(s) - min(d[0][n], d[1][n], d[2][n]))
