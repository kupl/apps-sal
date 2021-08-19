h, w = map(int, input().split())
[print("#", end="") for j in range(w + 2)]
print()
for i in range(h):
    print("#" + input() + "#")
[print("#", end="") for j in range(w + 2)]
