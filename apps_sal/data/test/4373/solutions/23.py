n = int(input())
mas = [int(i) for i in input().split()]
mas = sorted(mas)
k = 1
for i in range(n):
    if mas[i] >= k:
        k += 1
print(k - 1)
