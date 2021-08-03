q = int(input())
for rwerwe in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [b[i] - a[i] for i in range(n)]
    dupa = {}
    for i in range(n):
        if c[i] != 0:
            dupa[c[i]] = 0
    if len(dupa) > 1:
        print("NO")
    if len(dupa) == 0:
        print("YES")
    if len(dupa) == 1:
        if sum(c) < 0:
            print("NO")
        else:
            for i in range(n):
                if c[i] != 0:
                    start = i
                    break
            for j in range(n):
                i = n - 1 - i
                if c[j] != 0:
                    end = j
            if (end - start + 1) * c[start] == sum(c):
                print("YES")
            else:
                print("NO")
