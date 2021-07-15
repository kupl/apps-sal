n = int(input())
x1, x2 = list(map(int, input().split()))
x1 += 10**-8
x2 -= 10**-8
lines = []
for i in range(n):
    lines.append(list(map(int, input().split())))

ord_left = []
ord_right = []
for i in range(n):
    ord_left.append(lines[i][0] * x1 + lines[i][1])
    ord_right.append(lines[i][0] * x2 + lines[i][1])


enum_l = list(range(n))
enum_r = list(range(n))
enum_l.sort(key=lambda ord: ord_left[ord])
enum_r.sort(key=lambda ord: ord_right[ord])



if enum_l == enum_r:
    print("NO")
else:
    print("YES")
# for i in range(len(ord_right)):
#   line = ord_left[i][0]

