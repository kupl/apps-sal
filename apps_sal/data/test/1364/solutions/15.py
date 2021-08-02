n = int(input())
sushi = [int(x) for x in input().split()]
sushi.append(3)
tot = []
counter = 1
for i in range(1, n + 1):
    if sushi[i] == sushi[i - 1]:
        counter += 1
    else:
        tot.append(counter)
        counter = 1
answer = 0
for i in range(1, len(tot)):
    answer = max(answer, min(tot[i], tot[i - 1]) * 2)
print(answer)
