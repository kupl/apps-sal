(n, k) = list(map(int, input().split()))
num = list(map(int, input().split()))
gay = []
for i in num:
    gay.append(i % k)
number = [0] * 101
for i in gay:
    number[i] += 1
i = 0
chuj = 1
wynik = 0
while i < k:
    if i == (k - i) % k:
        if number[i] > 1:
            number[i] -= 2
            wynik += 1
        else:
            number[i] = 0
            i += 1
    else:
        if number[i] > 0:
            if number[(k - i) % k] > 0:
                number[i] -= 1
                number[(k - i) % k] -= 1
                wynik += 1
            else:
                number[i] = 0
        if number[i] == 0:
            i += 1
print(2 * wynik)
