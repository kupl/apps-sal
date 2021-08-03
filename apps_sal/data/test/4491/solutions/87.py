n = int(input())
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]

candy_max = 0

for i in range(n + 1):
    candies = sum(a1[0:i + 1]) + sum(a2[i:n])
    if candy_max < candies:
        candy_max = candies

print(candy_max)
