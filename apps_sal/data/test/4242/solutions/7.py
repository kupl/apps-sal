(a, b, k) = map(int, input().split())
list01 = []
for i in reversed(range(1, 101)):
    if a % i == 0 and b % i == 0:
        list01.append(i)
    else:
        pass
print(list01[k - 1])
