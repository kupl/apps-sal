n, m = list(map(int, input().split()))
arr = [0 for i in range(n)]
sq = list(map(int, input().split()))
for c in sq: arr[c - 1] += 1
print(min(arr))

