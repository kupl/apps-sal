from sys import stdin

k, r = list(map(int, stdin.readline().split()))

for n in range(1, 10):
    if (n * k) % 10 == r or (n * k) % 10 == 0:
        print(n)
        break
else:
    print(10)
