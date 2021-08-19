from bisect import bisect_left
v = []
i = 0
while True:
    st = bin(i).replace('0b', '')
    k = num = 0
    for j in range(len(st) - 1, -1, -1):
        num += int(st[j]) * pow(3, k)
        k += 1
    if num > 100000:
        break
    v.append(num)
    i += 1
v.sort()
for _ in range(int(input())):
    n = int(input())
    idx = bisect_left(v, n)
    print(v[idx])
