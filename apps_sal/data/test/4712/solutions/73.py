h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())
for _ in range(w + 2):
    print("#", end="")
print()
for i in range(h):
    print("#", end="")
    print(a[i], end="")
    print("#")
for _ in range(w + 2):
    print("#", end="")
