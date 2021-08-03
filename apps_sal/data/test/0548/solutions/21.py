n = int(input())
l = list(map(int, input().split()))
s = sum(l)
if s % 2 == 1:
    print("First")
    return
else:
    o = 0
    e = 0
    for i in range(n):
        if l[i] % 2 == 0:
            e += 1
        else:
            o += 1
    if o == 0:
        print("Second")
    else:
        print("First")
