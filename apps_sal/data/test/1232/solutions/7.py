n1, n2 = map(int, input().split())
m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[m - 1] < b[-k]:
    print("YES")
else:
    print("NO")
