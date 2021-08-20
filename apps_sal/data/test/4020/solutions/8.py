(a, b) = map(int, input().split(':'))
(c, d) = map(int, input().split(':'))
s = a * 60 + b
f = c * 60 + d
ans = s + (f - s) // 2
ansh = str(ans // 60)
ansm = str(ans % 60)
print('0' * (2 - len(ansh)) + ansh, '0' * (2 - len(ansm)) + ansm, sep=':')
