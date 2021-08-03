n = int(input())
arr = list(map(int, input().split()))

for _ in range(n - 1):
    arr.sort()
    new_v = (arr[0] + arr[1]) / 2
    del arr[0:2]
    arr.append(new_v)

print((arr[0]))
