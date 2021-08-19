(n, k) = map(int, input().split(' '))
mas = list(map(int, input().split(' ')))
submas = [10 - i % 10 if i < 100 else 11 for i in mas]
summ = 0
for i in mas:
    summ += i // 10
submas.sort()
for i in submas:
    if k >= i and i <= 10:
        k -= i
        summ += 1
    else:
        break
if k >= 10:
    for i in range(n):
        if mas[i] < 100:
            mas[i] = mas[i] + 10 - mas[i] % 10
        if k >= 100 - mas[i]:
            summ += (100 - mas[i]) // 10
            k -= 100 - mas[i]
        else:
            summ += k // 10
            break
print(summ)
