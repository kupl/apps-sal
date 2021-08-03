tests = int(input())
for test in range(tests):
    n = int(input())
    a = [int(i) for i in input().split()]
    l, r = -1, -1
    ans = 1
    for i in range(n):
        if r == -1:
            if l == -1:
                if a[i] != i + 1:
                    if l == -1:
                        l = i
            else:
                if a[i] == i + 1:
                    if r == -1:
                        r = i - 1
        else:
            if a[i] != i + 1:
                ans = 2
                break
    if l == -1:
        print(0)
    else:
        print(ans)
