n, k = map(int, input().split())
a = input()
pos = -1
for i in range(n):
    if a[i] == "G":
        pos = i
        break
for i in range(pos, len(a), k):
    if a[i] == "T":
        print("YES")
        return
    if a[i] == "#":
        break
for i in range(pos, -1, -k):
    if a[i] == "T":
        print("YES")
        return
    if a[i] == "#":
        break
print("NO")
