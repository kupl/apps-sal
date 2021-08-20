n = int(input())
m = int(input())
n = n % 6
o = 0
for i in range(n):
    if i % 2 == 1:
        if o != 0:
            o = 3 - o
    elif o != 2:
        o = 1 - o
if o == m:
    print(0)
else:
    o = 1
    for i in range(n):
        if i % 2 == 1:
            if o != 0:
                o = 3 - o
        elif o != 2:
            o = 1 - o
    if o == m:
        print(1)
    else:
        print(2)
