import bisect
x = int(input())

i = 1
cum = [0]
while cum[-1] < 10**9:
    cum += [cum[-1] + i]
    i += 1

index = bisect.bisect_left(cum, x)

print(index)
