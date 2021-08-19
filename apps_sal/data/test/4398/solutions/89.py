input()
print(''.join((lambda x: (x[0][i] + x[1][i] for i in range(len(x[0]))))(input().split())))
