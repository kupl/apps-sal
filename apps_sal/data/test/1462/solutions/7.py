import collections


n, k = list(map(int, str.split(input())))
coins = 0
for _, count in collections.Counter(input()).most_common():

    count = min(count, k)
    coins += count ** 2
    k -= count
    if k == 0:

        break

print(coins)
