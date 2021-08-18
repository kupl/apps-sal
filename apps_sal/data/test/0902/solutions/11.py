n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))
mx = max(ar)
winns = {x: 0 for x in ar}
while True:
    if ar[0] > ar[1]:
        if(ar[0] == mx or winns[ar[0]] >= k - 1):
            print(ar[0])
            break
        ar.append(ar.pop(1))

    else:
        ar.append(ar.pop(0))
    winns[ar[0]] += 1
