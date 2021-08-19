import bisect
list = []
for i in range(1, 10 ** 5):
    list.append((3 * i ** 2 + i) // 2)
for _ in range(int(input())):
    n = int(input())
    count = 0
    while n >= 2:
        r = bisect.bisect_right(list, n)
        n -= list[r - 1]
        count += 1
    print(count)
