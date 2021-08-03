h, w = map(int, input().split())
a = [[]]
print("#" * (w + 2))
for _ in range(h):
    print("#", input().strip(), "#", sep="")
print("#" * (w + 2))
