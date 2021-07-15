K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
    return

start = j = 7 % K
count = 1

#無限ループ
while True:
    #0の時
    if j == 0:
        print(count)
        return
        
    j = 10 * j + 7
    j = j % K
    count += 1
    
    #同じ数のループしているかチェック
    if j == start:
        print(-1)
        return
