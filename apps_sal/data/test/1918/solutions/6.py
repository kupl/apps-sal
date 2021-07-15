n = int(input())
prices = list(map(int, input().split()))
who = input()
basic = 0
for i in range(len(who)):
    if who[i] == "B":
        basic += prices[i]
max = basic
now = basic
for i in range(len(who)):
    if who[i] == "A":
        now += prices[i]
    else:
        now -= prices[i]
    if now > max:
        max = now
now = basic
for i in range(len(who) - 1, -1, -1):
    if who[i] == "A":
        now += prices[i]
    else:
        now -= prices[i]
    if now > max:
        max = now
print(max)
