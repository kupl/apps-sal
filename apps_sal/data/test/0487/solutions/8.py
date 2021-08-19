n = int(input())
arr = list(map(int, input().split()))
k = max(arr)
a = sum(arr)
b = 0
while b <= a:
    b = sum((k - x for x in arr))
    k += 1
print(k - 1)
