n = int(input())
r = n % 1000
if r == 0:
    print('0')
else:
    otu = 1000 - r
    print(otu)
