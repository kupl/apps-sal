
import sys
# sys.stdin=open("data.txt")
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ax1 = min(a[::2])
ax2 = max(a[::2])
ay1 = min(a[1::2])
ay2 = max(a[1::2])

bx1 = min(b[::2])
bx2 = max(b[::2])
by = 0
for i in range(4):
    if b[i * 2] == bx1:
        by = b[i * 2 + 1]

has = 0
for i in range(ax1, ax2 + 1):
    for j in range(ay1, ay2 + 1):
        # check this point
        if i < bx1 or i > bx2: continue
        if bx1 <= i <= (bx1 + bx2) // 2 and abs(j - by) <= abs(i - bx1):
            has = 1
        if (bx1 + bx2) // 2 <= i <= bx2 and abs(j - by) <= abs(i - bx2):
            has = 1
print("YES" if has else "NO")
