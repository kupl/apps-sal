N = int(input())
A = list(map(int, input().split()))
pos = 0
now = 0
for (i, a) in enumerate(A):
    now += a
    if i % 2 == 0:
        if now <= 0:
            pos += -now + 1
            now = 1
    elif now >= 0:
        pos += now + 1
        now = -1
neg = 0
now = 0
for (i, a) in enumerate(A):
    now += a
    if i % 2 == 0:
        if now >= 0:
            neg += now + 1
            now = -1
    elif now <= 0:
        neg += -now + 1
        now = 1
print(min(pos, neg))
