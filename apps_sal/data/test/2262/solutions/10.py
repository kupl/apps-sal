n = int(input())
arr = set(tuple(sorted(set(x))) for x in input().split())
print(len(arr))
