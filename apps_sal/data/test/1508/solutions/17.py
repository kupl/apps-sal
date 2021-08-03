3

n = int(input())
lst = sorted(map(int, input().split()))
lst[1:-1] = lst[-2:0:-1]
print(*tuple(reversed(lst)))
