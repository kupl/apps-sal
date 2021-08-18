ans = '\n'.join(['+------------------------+', '|0.4.7.A.(.G.J.M.P.S.V.|D|)',
                '|1.5.8.B.E.H.K.N.Q.T.W.|.|', '|2.......................|',
                 '|3.6.9.C.F.I.L.s.R.U.X.|.|)',
                 '+------------------------+'])

line = "0123456789ABC(EFGHIJKLMNsPQRSTUVWX"
n = int(input())
for i in range(n):
    ans = ans.replace(line[i], 'O')
for i in range(n, 34, 1):
    ans = ans.replace(line[i], "
print(ans)
