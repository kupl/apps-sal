# cook your dish here

jacketCost, sockCost, money = list(map(int, input().split()))

remainingMoney = money - jacketCost
PairOfsocks = remainingMoney // sockCost


if PairOfsocks % 2 == 1:
    print("Unlucky Chef")
else:
    print("Lucky Chef")
