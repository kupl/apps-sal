n, k, x = list(map(int, input().split()))
mas = list(map(int, input().split()))
print(k * x + sum(mas[:-k]))
