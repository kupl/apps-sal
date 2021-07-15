n = int(input())
flag = False
for a in range(1, 40):
    for b in range(1,40):
        if 3**a + 5**b == n:
            print(a, b)
            flag = True
            break
    if flag:
        break
else:
    print(-1)
