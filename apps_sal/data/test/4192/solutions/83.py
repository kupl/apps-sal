#!/usr/bin/env python3
# 誤差対策で掛け算にする
d, t, s = list(map(int, input().split()))
print(("Yes" if d <= t * s else "No"))
