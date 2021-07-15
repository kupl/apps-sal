#アライグマはモンスターと戦っています。
# モンスターの体力は H です。
#アライグマは N 種類の必殺技を使うことができ、
#i 番目の必殺技を使うとモンスターの体力を Ai 減らすことができます。
#モンスターの体力を 0 以下にすればアライグマの勝ちです。

H,N=map(int,input().split())
A = list(map(int,input().split()))

if H - sum(A) <= 0:
    print("Yes")
else:
    print("No")
