n = int(input())
a = input()
for i in range(n - 1):
    if a[i] != a[i + 1]:
        print("YES")
        print(a[i] + a[i + 1])
        return
print("NO")
