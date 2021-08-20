n = int(input())
operations = 0
s = bin(n)[2:]
ans = []
while len(s) != s.count('1'):
    if operations % 2 == 0:
        x = s.find('0')
        x = len(s) - x
        n = n ^ 2 ** x - 1
        ans.append(x)
        operations += 1
        s = bin(n)[2:]
    else:
        n = n + 1
        s = bin(n)[2:]
        operations += 1
print(operations)
print(' '.join((str(x) for x in ans)))
