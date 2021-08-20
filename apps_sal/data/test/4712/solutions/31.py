(h, w) = list(map(int, input().split()))
pixel = [[] for i in range(h + 2)]
for i in range(h + 2):
    if i == 0:
        pixel[i].append('#' * (w + 2))
    elif i == h + 1:
        pixel[i].append('#' * (w + 2))
    else:
        pixel[i].append('#')
        s = input()
        pixel[i].append(s)
        pixel[i].append('#')
for i in range(h + 2):
    print(''.join(pixel[i]))
