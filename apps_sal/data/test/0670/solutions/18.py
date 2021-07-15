import math
a, b, c = list(map(int, input().split()))
ax, ay, bx, by = list(map(int, input().split()))
if (a==0 or b==0):
    print(abs(ax - bx) + abs(ay - by))
    return
oy = -(a*ax+c)/b
ty = -(a*bx+c)/b
ox = -(b*ay+c)/a
tx = -(b*by+c)/a
ans = abs(ax - bx) + abs(ay - by)
ans1 = abs(ay - oy) + abs(by - ty) + math.sqrt(abs(ax - bx)**2 + abs(oy - ty)**2)
ans2 = abs(ax - ox) + abs(bx - tx) + math.sqrt(abs(ay - by)**2 + abs(ox - tx)**2)
ans3 = abs(ax - ox) + abs(by - ty) + math.sqrt(abs(bx - ox)**2 + abs(ay - ty)**2)
ans4 = abs(ay - oy) + abs(bx - tx) + math.sqrt(abs(by - oy)**2 + abs(ax - tx)**2)
print(min(ans, ans1, ans2, ans3, ans4))

