total_integer = int(input())
integer = sorted(list(map(int, input().split())))
print(integer[total_integer - 1] - integer[0])
