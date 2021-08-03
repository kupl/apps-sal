a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
if max(e - a, e - b, e - c, e - d) <= k:
    print('Yay!')
else:
    print(':(')
