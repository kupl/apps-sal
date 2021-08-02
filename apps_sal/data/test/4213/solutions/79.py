n = int(input())  # Nを入力
lista = input().split()  # Aを入力
p = int(lista[0])  # p最小値
q = int(lista[0])  # q最大値
for i in range(1, n):
    k = int(lista[i])
    if k <= p:
        p = k
    elif k >= q:
        q = k
print(int(q - p))
