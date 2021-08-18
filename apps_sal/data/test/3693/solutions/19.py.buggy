mp = [[0 for i in range(205)]for j in range(205)]
ax1, ay1, ax2, ay2, ax3, ay3, ax4, ay4 = list(map(int, input().split()))
bx1, by1, bx2, by2, bx3, by3, bx4, by4 = list(map(int, input().split()))
ax1 += 100
ay1 += 100
ax2 += 100
ay2 += 100
ax3 += 100
ay3 += 100
ax4 += 100
ay4 += 100
bx1 += 100
by1 += 100
bx2 += 100
by2 += 100
bx3 += 100
by3 += 100
bx4 += 100
by4 += 100
x1 = min(ax1, ax2, ax3, ax4)
x2 = max(ax1, ax2, ax3, ax4)
y1 = min(ay1, ay2, ay3, ay4)
y2 = max(ay1, ay2, ay3, ay4)
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        mp[i][j] = 1
        # print(i,j)
# print()
xx = (bx1 + bx3) // 2
yy = (by1 + by3) // 2
r = abs(min(bx1, bx2, bx3, bx4) - xx)
for i in range(min(bx1, bx2, bx3, bx4), max(bx1, bx2, bx3, bx4) + 1):
    for j in range(min(by1, by2, by3, by4), max(by1, by2, by3, by4) + 1):
        # print(abs(i-xx),abs(j-yy))
        if abs(i - xx) + abs(j - yy) <= r:
            if mp[i][j] == 1:
                # print(i,j)
                print('YES')
                return
print('NO')
