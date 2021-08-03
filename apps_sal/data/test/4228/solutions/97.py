n, l = (int(i) for i in input().split())
list_ringo = [l + i - 1 for i in range(1, n + 1)]
if 0 in list_ringo:
    print(sum(list_ringo))
elif max(list_ringo) < 0:
    print(sum(list_ringo[:n - 1]))
else:
    print(sum(list_ringo[1:]))
