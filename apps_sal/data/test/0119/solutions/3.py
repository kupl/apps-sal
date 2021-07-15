n = int(input())

segments = []

for i, _ in enumerate(range(n)):
    a, b = map(int, input().split())
    segments.append(((a, b), i + 1))

segments.sort(key=lambda x: (x[0][0], -x[0][1]))

last_r = 0
last_index = 0

for segment, index in segments:
    if last_r >= segment[1]:
        print(index, last_index)
        break

    last_r = segment[1]
    last_index = index
else:
    print(-1, -1)
