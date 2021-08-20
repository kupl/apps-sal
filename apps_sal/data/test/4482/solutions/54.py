(N, *a) = open(0).read().split()
N = int(N)
list1 = list(map(int, a))
a = []
for i in range(-100, 101):
    int1 = 0
    for n in range(N):
        x = list1[n] - i
        y = x ** 2
        int1 += y
        if n == N - 1:
            a.append(int1)
print(min(a))
