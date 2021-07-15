N = int(input())
while True:
    check = True
    # sqrt(N)まで試し割りする
    # 割り切れたらnを増やしてもう一回
    for i in range(2,int(N**0.5)+1):
        if N%i == 0:
            N += 1
            check = False
            break
    if check:
        print(N)
        break

