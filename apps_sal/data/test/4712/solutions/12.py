h, w = map(int, input().split())
print("#" * (w + 2))
for i in range(h):
    a = str(input())
    a = "#" + a + "#"
    print(a)
print("#" * (w + 2))
