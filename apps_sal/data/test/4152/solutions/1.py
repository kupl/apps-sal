from collections import defaultdict

n = int(input())
a = [int(i) for i in input().split()]
arr = defaultdict(int)

for i in a:
    arr[i] += 1

powers = [1 << i for i in range(32)]
count = 0

x = list(arr.items())

for i, c in x:

    good = 0

    for p in powers:
        n = p - i
        if n == i:
            if arr[n] > 1:
                good = 1
                break
        else:
            if arr.get(n):
                good = 1
                break
    if good == 0:
        count += c

print(count)

