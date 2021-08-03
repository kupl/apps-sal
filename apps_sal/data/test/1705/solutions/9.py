n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(min(n - arr.index(1), n - arr.index(0)))
