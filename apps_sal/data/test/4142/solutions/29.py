S = input()
Odd = S[::2]
Even = S[1::2]
print('Yes' if Odd.count('L') == 0 and Even.count('R') == 0 else 'No')
