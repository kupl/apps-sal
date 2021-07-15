t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    if n%2 == 1:
        print("Second")
        continue
    for j in a:
        if j in d:
            d[j] = d[j]^1
        else:
            d[j] = 1
    # print(d)
    for j in d.keys():
        if d[j] == 1:
            print("First")
            break
    else:
        print("Second")
