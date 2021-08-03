n = input()
wa = 0
for i in range(0, 10):
    wa = wa + n.count(str(i)) * i
print('Yes' if wa % 9 == 0 else 'No')
