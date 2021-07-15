b = int(input())
g = int(input())
n = int(input())
wyn = 0
for bb in range(b + 1):
    if n - bb in range(g + 1):
        wyn += 1
print(wyn)
