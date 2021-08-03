hoge = input()
int_line = [int(i) for i in input().split()]

cnt = 0
flag = False

while True:
    for m, i in enumerate(int_line):
        if i % 2 == 0:
            int_line[m] = i / 2
        else:
            flag = True
    if flag == True:
        print(cnt)
        break
    else:
        cnt += 1
