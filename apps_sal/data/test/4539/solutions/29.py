a = input()
x = [int(i) for i in a]
print('Yes' if int(a) % sum(x) == 0 else 'No')
