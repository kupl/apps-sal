n = int(input())
a = input().split(' ')
ca = 0
cb = 0
MAX = 0
MIN = 10000000000
for data in a:
    x = int(data)
    if x<MIN:
        cb = 1
        MIN = x
    elif x==MIN:
        cb += 1
    if x>MAX:
        MAX = x
        ca = 1
    elif x==MAX:
        ca += 1
if ca==n:
    print(MAX-MIN,' ',n*(n-1)>>1)
else:
    print(MAX-MIN,' ',ca*cb)
