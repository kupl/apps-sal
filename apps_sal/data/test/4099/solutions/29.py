N, K, M = map(int, input().split())
Alist = list(map(int, input().split()))

i = 0
temp = 0
flag = False
for i in range(0, K + 1):
    mean = (sum(Alist) + i) // N
    if M <= mean:
        temp = i
        flag = True
        break

if flag == True:
    print(temp)
else:
    print(-1)
