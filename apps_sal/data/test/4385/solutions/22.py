a = [int(input()) for _ in range(5)]
k = int(input())
flag = False
for i in range(5):
    for j in range(i + 1, 5):
        tmp = abs(a[i] - a[j])
        if tmp > k:
            flag = True
            break
    if flag:
        break
if flag:
    print(":(")
else:
    print("Yay!")
