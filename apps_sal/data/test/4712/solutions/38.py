h, w = map(int, input().split())

print("#" * (w + 2))

for i in range(h):
    num = input()
    print("#" + num + "#")

print("#" * (w + 2))
