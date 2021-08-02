import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
cards = sys.stdin.readline().strip()
count = [0] * 26
for letter in cards:
    count[ord(letter) - ord('A')] += 1
count.sort()
count.reverse()
coins = 0
i = 0
while k > 0 and i < 26:
    if count[i] <= k:
        coins += count[i] * count[i]
        k -= count[i]
    else:
        coins += k * k
        k = 0
    i += 1
print(coins)
