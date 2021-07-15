#ARC106 A

N = int(input())

#5 は**25でオーバー
#3 は**38でオーバー


for i in range(1,28):
    for j in range(1,40):
        ans = 5**i + 3**j
        if ans == N:
            print(j, i)
            return
            
print(-1)
