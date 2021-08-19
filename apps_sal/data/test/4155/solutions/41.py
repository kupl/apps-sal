n = int(input())
h = list(map(int, input().split()))
cnt = 0
grow = True
while grow:
    inc = False
    grow = False
    for i in range(n):
        if h[i] == 0:
            inc = False
        else:
            h[i] -= 1
            if not inc:
                inc = True
                grow = True
                cnt += 1
print(cnt)
