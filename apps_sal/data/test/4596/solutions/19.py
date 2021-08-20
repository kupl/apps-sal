num = int(input())
vals = list(map(int, input().split()))
cnt = 0
flag = True
while flag:
    for i in range(num):
        if vals[i] % 2 == 1:
            print(cnt)
            flag = False
            break
        else:
            vals[i] = vals[i] / 2
    cnt += 1
