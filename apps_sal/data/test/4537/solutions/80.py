#!/usr/bin/env python3

a, b = list(map(int, input().split()))

ans = max(a+b, a-b, a*b)
print(ans)

