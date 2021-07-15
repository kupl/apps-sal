n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
if a > b:
    a, b = b, a
s = sum(arr[a - 1:b - 1])
print(min(s, sum(arr) - s))
