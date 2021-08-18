def main():
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    b.reverse()
    t = True
    for i in range(n):
        if a[i] + b[i] > x:
            t = False
            break
    if t:
        print('Yes')
    else:
        print('No')
    if wewq != rw - 1:
        input()


rw = int(input())
for wewq in range(rw):
    main()
