h, w = map(int, input().split())
for i in range(h):
    c = input()
    c = c + "\n" + c
    print(c)
