n = int(input())
k = 0
lst = []

for i in range(n):
    lst = list(map(int, input().split()))
    if lst[1] - lst[0] >= 2:
        k =k+ 1
print(k)
