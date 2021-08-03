n = int(input())
ip = list(map(int, input().split()))
high = -10000000
for i in ip:
    if i > high:
        if i < 0:
            high = i
        else:
            if (i**0.5) % 1 == 0:
                pass
            else:
                high = i
print(high)
