import math
(cat, meta, x) = map(int, input().split())
if cat > x or cat + meta < x:
    print('NO')
else:
    print('YES')
