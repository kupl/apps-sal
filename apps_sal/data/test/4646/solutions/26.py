for _ in range(int(input())):
    am = int(input())
    arr = list(map(int, input().split()))
    bad = [0, 0]
    fl = False
    for i in range(am):
        if arr[i] & 1 != i & 1:
            bad[i & 1] += 1
            fl = True
    if not fl:
        print(0)
    elif bad[0] != bad[1]:
        print(-1)
    else:
        print(bad[0])
