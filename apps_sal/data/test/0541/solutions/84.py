#!/usr/bin/env python3

n, m = list(map(int, input().split()))

# for i in range():

ab = [list(map(int, input().split())) for _ in range(m)]

ab.sort()
# print(ab)
ans = 0
div = -1, -1
for i in range(len(ab)):
    a, b = ab[i]
    # print(a, b)

    if a == div[0]:
        continue
    elif a >= div[1]:
        div = a, b
        ans += 1
    else:
        div = a, min(b, div[1])
    # print(div, ans)

print(ans)
