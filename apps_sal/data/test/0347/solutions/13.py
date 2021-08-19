import sys
arr1 = [int(x) for x in sys.stdin.readline().split()]
arr2 = [int(x) for x in sys.stdin.readline().split()]
base = [500, 1000, 1500, 2000, 2500]
res = 0
for i in range(5):
    res += max([0.3 * base[i], base[i] * (1 - arr1[i] / 250) - 50 * arr2[i]])
(a, b) = [int(x) for x in sys.stdin.readline().split()]
res += 100 * a
res -= 50 * b
print(int(res))
