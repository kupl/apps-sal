w = input()
a = 0
for i in range(97, 124):
    cnt = 0
    for j in w:
        if j == chr(i):
            cnt += 1
    if cnt % 2 != 0:
        print("No")
        break
    else:
        a += 1
        if a == 27:
            print("Yes")
            break
