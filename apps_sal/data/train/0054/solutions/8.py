q = int(input())
for rew in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    while True:
        if 2048 in l:
            print("YES")
            break
        if len(l) == 0:
            print("NO")
            break
        if len(l) > 1 and l[0] == l[1]:
            l = [2 * l[0]] + l[2:]
        else:
            l = l[1:]
        l.sort()
