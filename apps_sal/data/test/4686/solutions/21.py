w = input()
re = [w.count(i) for i in w]
print('Yes' if all((i % 2 == 0 for i in re)) else 'No')
