n = int(input())
a = sorted(list(map(int, input().split())))
if n % 2 == 0:
    b, s = [1, 1], 3
else:
    b, s = [0], 2
for i in range(s, n, 2):
    b += [i, i]
if a == b:
    print(pow(2, n // 2, 1000000007))
else:
    print(0)
