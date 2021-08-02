s = int(input())
a = [int(i) for i in input().split()]
for idx, num in enumerate(a):
    if a[a[num - 1] - 1] == idx + 1:
        print("YES")
        return
print("NO")
