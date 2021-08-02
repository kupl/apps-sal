def naek(a, indeks):
    for x in range(indeks, len(a) - 1):
        if a[x] > a[x + 1]:
            return False
            pass
        pass
        pass
    return True
    pass


a = int(input())
a = list(map(int, input().split(" ")))
sor = True
for x in range(len(a) - 1):
    if a[x] > a[x + 1]:
        sor = False
        idx = x + 1
        break
        pass
    pass

if sor:
    print(0)
else:
    if naek(a, idx):
        if a[len(a) - 1] > a[0]:
            print(-1)
        else:
            print(len(a) - idx)
            pass
        pass
    else:
        print(-1)
    pass
