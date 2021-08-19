a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
d1 = b - a
d2 = c - a
d3 = d - a
d4 = e - a
d5 = c - b
d6 = d - b
d7 = e - b
d8 = d - c
d9 = e - c
d10 = e - d
if d1 > k or d2 > k or d3 > k or (d4 > k) or (d5 > k) or (d6 > k) or (d7 > k) or (d8 > k) or (d9 > k) or (d10 > k):
    print(':(')
else:
    print('Yay!')
