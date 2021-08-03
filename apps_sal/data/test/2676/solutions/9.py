n = int(input())

pile = []

for i in range(n):
    pile.append(input())

m = int(input())

st = input()


ans = 0
for i in set(pile):
    if i in st:
        ans += 1


print(ans)
