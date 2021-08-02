# モンスターの体力は H
# アライグマの必殺技は N 種類
# アライグマが同じ必殺技を 2 度以上使うことなく
# モンスターに勝つことができるなら Yes を、
# できないなら No を出力。

H, N = map(int, input().split())
A = list(map(int, input().split()))
answer = sum(A)

if H <= answer:
    print("Yes")
else:
    print("No")
