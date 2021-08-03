n = int(input())
a = list(map(int, input().split()))
if max(a) != min(a):
    while a.count(0) != len(a) - 1:
        a.sort()
        b = [a[0]]
        for i in a[1:]:
            if i % a[0] != 0:
                b.append(i % a[0])
        a = b
    print(max(a))
else:
    print(a[0])
