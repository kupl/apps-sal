k, x = map(int, input().split())
list01 = []
for i in range(1 + x - k, 0 + x + k):
    if -1000000 <= i <= 1000000:
        list01.append(i)
print(' '.join(map(str, list01)))
