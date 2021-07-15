x = int(input())

gold_coin = x // 500
left_coin = x % 500
bronze_coin = left_coin // 5

happiness = gold_coin * 1000 + bronze_coin * 5
print(happiness)
