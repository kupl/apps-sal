A, B = map(int, input().split())
flag = True
for i in range(1, 1010):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        flag = False
        break
if flag:
    print(-1)
