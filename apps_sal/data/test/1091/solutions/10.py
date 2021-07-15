input()
bet = [int(i) for i in input().split()]
x = bet.index(max(bet)) + 1
bet.sort()
print(x, bet[-2])
