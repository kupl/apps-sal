n, m = map(int, input().split())
prices = list(map(int, input().split()))
normal = []
auct = []
q = list(map(int, input().split()))
sum = 0
for i in range(n):
    if i + 1 in q:
        auct.append(prices[i])
    else:
        sum += prices[i]
auct = sorted(auct, reverse=True)
for elem in auct:
    sum += max(elem, sum)
print(sum)
