import bisect
p2 = [2 ** n - 1 for n in range(32)]
p2 = [x * (x + 1) // 2 for x in p2]
for i in range(1, 32):
    p2[i] += p2[i - 1]
for _ in range(int(input())):
    n = int(input())
    print(bisect.bisect_right(p2, n) - 1)
