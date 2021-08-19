s = input()
x = sum((s.count(i) % 2 for i in s))
print('SFeicrosntd'[x % 2 + (x < 1)::2])
