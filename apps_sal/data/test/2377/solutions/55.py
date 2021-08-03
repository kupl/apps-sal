n, h = list(map(int, input().split()))
cut = 0
throw = []

for i in range(n):
    a, b = list(map(int, input().split()))
    cut = max(cut, a)
    throw.append(b)

throw.sort(reverse=True)
throw_cam = []
for i in range(n):
    if cut > throw[i]:
        break
    if i == 0:
        throw_cam.append(throw[0])
    else:
        throw_cam.append(throw[i] + throw_cam[i - 1])

if throw_cam[len(throw_cam) - 1] < h:
    rh = h - throw_cam[len(throw_cam) - 1]
    if rh % cut == 0:
        print((len(throw_cam) + rh // cut))
    else:
        print((len(throw_cam) + rh // cut + 1))
else:
    for i in range(len(throw_cam)):
        d = throw_cam[i]
        if d >= h:
            print((i + 1))
            break
