laziness = []
for i in range(int(input())):
    laziness.append(int(input()))
laziness.sort()
j = len(laziness) - 1
sum = 0
for numb in laziness:
    sum += numb * laziness[j]
    j -= 1
print(sum % 10007)
