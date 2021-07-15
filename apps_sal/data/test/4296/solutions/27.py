a1, a2, a3 = [int(n) for n in input().split()]

print('bust' if a1+a2+a3 >= 22 else 'win')
