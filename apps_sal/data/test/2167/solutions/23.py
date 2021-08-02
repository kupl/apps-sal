n = input()
mas = input()
mas = mas.split(' ', int(len(mas) + 1 / 2))
mas = list(map(int, mas))
k = sum(mas) / len(mas)
if (k % 1 == 0):
    print(len(mas))
else:
    print(len(mas) - 1)
