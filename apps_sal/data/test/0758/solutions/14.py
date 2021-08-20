n = int(input())
s = list(input())
o = 0
try:
    index = s.index('B')
    o += pow(2, index)
    while True:
        index = s.index('B', index + 1)
        o += pow(2, index)
except:
    print(o)
