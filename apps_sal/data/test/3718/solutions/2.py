3

n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

for i in range(len(a) - 2):
    if a[i + 1] == a[i] + 1 and a[i + 2] == a[i] + 2:
        print("YES")
        return

print("NO")

