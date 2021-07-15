n = int(input())

lst = [int(x) for x in input().split()]

lst.sort()

print(lst[n - 1] - lst[0] - n + 1)



