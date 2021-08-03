n = int(input())
print(max([min(int(x) - 1, 10**6 - int(x)) for x in input().split()]))
