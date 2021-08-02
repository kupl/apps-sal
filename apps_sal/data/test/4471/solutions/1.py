q = int(input())
for rwe in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    dasie = True
    for i in range(1, n):
        if (l[i] - l[i - 1]) % 2 == 1:
            dasie = False
    if dasie:
        print("YES")
    else:
        print("NO")
