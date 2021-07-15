h, w = map(int, input().split())
a = [input() for _ in range(h)]
for i in range(h+2):
    if i == 0 or i == h+1:
        print("#"*(w+2))
    else:
        print("#" + a[i-1] + "#")
