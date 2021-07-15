abcde = [input() for i in range(5)]

k = int(input())

for ii in range(5):
    for jj in range(ii, 5):
        if int(abcde[jj]) - int(abcde[ii]) > k:
            print(':(')
            return

print('Yay!')
