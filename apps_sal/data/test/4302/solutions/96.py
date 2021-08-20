(A, B) = map(int, input().split())
coin_list = []
COIN1 = A + A - 1
COIN2 = B + B - 1
COIN3 = A + B
coin_list.append(COIN1)
coin_list.append(COIN2)
coin_list.append(COIN3)
print(max(coin_list))
