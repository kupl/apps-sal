n, c = list(map(int, input().split()))
lst = [int(x) for x in input().split()][::-1]

for i in range(len(lst) - 1):
    if lst[i] - lst[i + 1] > c:
        print(i + 1)
        break
else:
    print(len(lst))
