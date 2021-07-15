#解説を見て間違っていることに気がついた
#0は含まない！
N = int(input())
flag = True
for i in range(1,1000):
    for j in range(1,1000):
        if 3**i+5**j == N:
            print(i,j)
            flag = False
if flag:
    print(-1)
