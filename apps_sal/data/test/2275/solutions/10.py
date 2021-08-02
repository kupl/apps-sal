t = int(input())
for i in range(t):
    k = int(input())
    a = input()
    maxlen = 0
    cl = -1
    for i in a:

        if i == "A":
            cl = 0
        elif cl != -1:
            cl += 1
            maxlen = max(cl, maxlen)
    print(max(maxlen, 0))
