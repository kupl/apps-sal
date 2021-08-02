n = input()
print('Yes') if int(n) % sum([int(i) for i in n]) == 0 else print('No')
