n = int(input())
A = [int(x) for x in input().split()]
s = {A[0]}
left = 1
segments = []
for i in range(1, n):
    if A[i] in s:
        segments.append((left, i + 1))
        left = i + 2
        s.clear()
    else:
        s.add(A[i])
if len(segments) == 0:
    print(-1)
else:
    segments[-1] = (segments[-1][0], n)
    print(len(segments))
    for l, r in segments:
        print(l, r)
