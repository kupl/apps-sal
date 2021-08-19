h, w = map(int, input().split())
s = [""] * h
for i in range(h):
    s[i] = input()
print("#" * (w + 2))
for i in range(h):
    print("#" + s[i] + "#")
print("#" * (w + 2))
