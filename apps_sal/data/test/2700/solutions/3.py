t = int(input())
while t > 0:
    t = t - 1
    a, b, c, d = list(map(int, input().split()))
    count = 0
    for x in range(a, b + 1):
        if x < c:
            count += d - c + 1
        elif x < d:
            count += d - x
        else:
            break
    print(count)
    # for i in range(a,b+1):
    #   for j in range(c,d+1):
    #       if i<j:
    #           count += 1
    # print count
