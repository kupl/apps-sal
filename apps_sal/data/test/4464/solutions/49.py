A, B, C = list(map(int, input().split()))
#kA%Bの数列になる
#AをBで割ったあまりはB-1以下になる
#(k+B)A%B = (kA+BA)%B = kA%B + BA%B = kA%B
for i in range(1, B+1):
    if A*i%B == C:
        print('YES')
        return
print('NO')

