N = int(input())
d = [int(input()) for i in range(N)]

original = []
for i in d:
    if i not in original:
        original.append(i)
print((len(original)))
