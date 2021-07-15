n = input()
Li = input()
ar = map(int, Li.split())
res = -1
fl = 1
for i in ar:
    while i%2 == 0:
        i = i/2
    while i%3 == 0:
        i = i/3
    if res == -1:
        res = i
    elif res != i:
        fl = 0
if fl == 1:
    print ("Yes\n")
else:
    print ("No\n")
