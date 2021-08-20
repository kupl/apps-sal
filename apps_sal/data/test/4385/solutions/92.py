details = []
for i in range(6):
    details.append(int(input()))
checker = []
for i in details[:len(details) - 1]:
    for j in details[:len(details) - 1]:
        checker.append(j - i)
if max(checker) > details[-1]:
    print(':(')
else:
    print('Yay!')
