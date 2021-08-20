(n, a) = map(int, input().split())
criminals = list(map(int, input().split()))
i = j = a - 1
amount = 0
while i >= 0 and j < n:
    if criminals[i] == criminals[j] == 1:
        amount += 1 if i == j else 2
    i -= 1
    j += 1
while i >= 0:
    amount += criminals[i]
    i -= 1
while j < n:
    amount += criminals[j]
    j += 1
print(amount)
