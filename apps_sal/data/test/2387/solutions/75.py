N = int(input())
S1 = []
S2 = []
for i in range(N):
    S = input()
    (mid, end) = (0, 0)
    for s in S:
        if s == '(':
            end += 1
        else:
            end -= 1
        mid = min(mid, end)
    if end > 0:
        S1.append((mid, end))
    else:
        S2.append((mid - end, -end))
S1.sort(reverse=True)
S2.sort(reverse=True)
mid = end1 = 0
out = False
for t in S1:
    (a, b) = t
    mid = end1 + a
    end1 = end1 + b
    if mid < 0:
        out = True
        break
mid = end2 = 0
for t in S2:
    (a, b) = t
    mid = end2 + a
    end2 = end2 + b
    if mid < 0:
        out = True
        break
if not end1 == end2 or out:
    print('No')
else:
    print('Yes')
