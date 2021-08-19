N = int(input())
h = list(map(int, input().split()))
h.append(0)
pre = True
next = True
cnt = 0
for i in range(N):
    if h[i + 1] > h[i]:
        next = True
        if pre == False:
            cnt -= h[i]
    elif h[i + 1] < h[i]:
        next = False
        if pre == True:
            cnt += h[i]
    else:
        next = pre
    pre = next
print(cnt)
