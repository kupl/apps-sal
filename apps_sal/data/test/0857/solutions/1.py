a, b = input().split()
a, b = int(a), int(b)

arr = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for i in arr:
    if i in a2:
        print(i, end=' ')

