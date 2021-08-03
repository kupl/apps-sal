n, k = list(map(int, input().split()))

if k % 2 == 0:
    # Gu Su
    down = int(k / 2 + 1)
    if down > n:
        print(0)
        return
    else:
        up = min(k - 1, n)
        print(up - down + 1)
else:
    # Ki Su
    down = int((k + 1) / 2)
    if down > n:
        print(0)
        return
    else:
        up = min(k - 1, n)
        print(up - down + 1)

# print(down)
# print(up)
