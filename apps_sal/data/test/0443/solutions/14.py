n = int(input())
a = list(map(int, input().split()))
if len(a) == 1:
    print(-1)
elif len(a) == 2 and a[0] == a[1]:
    print(-1)
else:
    mina = min(a)
    for (i, x) in enumerate(a):
        if x == mina:
            print(1)
            print(i + 1)
            break
