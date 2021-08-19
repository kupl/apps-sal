#!/usr/bin/env python3

N, S = list(map(int, input().split()))

stuff = [list(map(int, input().split())) for i in range(N)]
answer = S
for a, k in stuff:
    answer = max(answer, a + k)

print(answer)
