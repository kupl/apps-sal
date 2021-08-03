h, w = map(int, input().split())

s = "#" * (w + 2)

print(s)
for i in range(h):
    t = input()
    print("#", end="")
    print(t, end="#\n")
print(s)
