def solve():
    kek = input()
    a = sorted(list(map(int, input().split())))
    if a[0] == a[-1]:
        print(len(a))
    else:
        print(1)


[solve() for x in range(int(input()))]

