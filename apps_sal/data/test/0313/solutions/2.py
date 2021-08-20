n = int(input())
mas = list(map(int, input().split(' ')))
p = 0
res = 0
for i in range(n):
    if mas[i] == 0:
        if i > 0 and i < n - 1:
            if mas[i - 1] == 1 and mas[i + 1] == 1:
                mas[i] = 1
print(sum(mas))
