n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
s = 0
for i in arr:
    s += m - i
print(s)
