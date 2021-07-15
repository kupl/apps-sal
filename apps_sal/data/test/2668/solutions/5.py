# cook your dish here
jacketCost, sockCost, money=map(int, input().split())
money=money-jacketCost
if (money//sockCost)%2==0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")

