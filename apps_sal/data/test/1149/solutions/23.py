n = int(input())
s = input().strip().split()
w = input().strip().split()
p = int(s[0])
q = int(w[0])
if p + q < n:
    print("Oh, my keyboard!")
else:
    d = {}
    for i in s[1:]:
        d[int(i)] = 1
    ack = p
    for i in w[1:]:
        try:
            d[int(i)] += 1
        except KeyError:
            d[int(i)] = 1
            ack += 1
    if ack < n:
        print("Oh, my keyboard!")
    else:
        print("I become the guy.")
