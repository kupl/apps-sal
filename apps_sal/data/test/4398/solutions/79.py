input()
print(''.join((lambda x, y: (x[i] + y[i] for i in range(len(x))))(*input().split())))
