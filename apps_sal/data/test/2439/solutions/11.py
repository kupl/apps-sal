from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    lst = list(int(x) for x in stdin.readline().split())

    if sum(lst) > 0:
        lst.sort(reverse=True)
        print("YES")
        print(' '.join(str(x) for x in lst))
    elif sum(lst) < 0:
        lst.sort()
        print("YES")
        print(' '.join(str(x) for x in lst))
    else:
        print("NO")

