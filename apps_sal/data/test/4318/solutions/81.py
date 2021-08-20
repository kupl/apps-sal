N = int(input())
H = list(map(int, input().split()))
result = 1
H.reverse()
HH = H.copy()
for i in H:
    HH.remove(i)
    if len(HH) == 0:
        break
    for ii in HH:
        if i < ii:
            break
    else:
        result += 1
print(result)
