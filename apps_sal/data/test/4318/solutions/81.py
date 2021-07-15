N = int(input())
H = list(map(int, input().split()))
result = 1 # 先頭の+1

H.reverse() # 計算しやすいように並び変える
HH = H.copy()

for i in H:
    HH.remove(i)

    if len(HH) == 0:
        break

    for ii in HH:
        if i < ii:
            break
    else:
        #print(i)
        result += 1


print(result)
