(a, b) = input().split()
hd = 'HD'
print(hd[(hd.index(a) + hd.index(b)) % 2])
