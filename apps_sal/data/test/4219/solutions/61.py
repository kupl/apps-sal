N = int(input())
Alist = []
xylists = []
for i in range(N):
    A = int(input())
    Alist.append(A)
    xylist = []
    for j in range(A):
        xylist.append(tuple(map(int, input().split())))
    xylists.append(xylist)
ans = 0
for bit in range(1 << N):
    HOU = list(reversed(list(format(bit, 'b').zfill(N))))
    notans = False
    for i in range(N):
        if bit & 1 << i:
            for (x, y) in xylists[i]:
                if HOU[x - 1] != str(y):
                    notans = True
                    break
            else:
                continue
            break
        else:
            continue
        break
    if not notans:
        ans = max(ans, str(bin(bit)).count('1'))
print(ans)
