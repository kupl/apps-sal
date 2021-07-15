n = int(input())
s = sum(map(int,list(str(n))))
print('Yes' if n%s == 0 else 'No')
