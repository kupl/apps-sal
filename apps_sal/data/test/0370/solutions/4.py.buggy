k = int(input())
x, y = [int(item) for item in input().split()]

# Think 1st quadrant
x_minus = False
if x < 0:
    x *= -1
    x_minus = True
y_minus = False
if y < 0:
    y *= -1
    y_minus = True
# Think x >= y
y_lt_x = False
if y > x:
    x, y = y, x
    y_lt_x = True

# Even step cannot go to odd point
if k % 2 == 0 and (x + y) % 2 == 1:
    print(-1)
    return

step_num = ((x + y) + (k - 1)) // k
d = (step_num * k - x - y) // 2
while d != 0 and (k > x + d or k > y + d + x):
    step_num += 1
    d = (step_num * k - x - y) // 2
if step_num * k % 2 != (x + y) % 2:
    step_num += 1
    d = (step_num * k - x - y) // 2

# print(x, y, step_num, step_num * k)

ans = []
step_len = 0
on_top = False
for i in range(step_num):
    step_len += k
    if step_len <= y + d:
        ans.append([0, step_len])
    elif step_len <= y + d + x:
        on_top = True
        ans.append([step_len - y - d, y + d])
    else:
        ans.append([x, (y + d) - (step_len - y - d - x)])
        if not on_top:
            newx, newy = ans[-1]
            prevx, prevy = ans[-2]
            if newy > prevy:
                b = abs(prevy - newy)
                a = k - abs(prevx - newx) - abs(prevy - newy)
                ans.pop()
                ans.append([newx + b + a // 2, newy - b - a // 2])
            else:
                a = k - abs(prevx - newx) - abs(prevy - newy)
                ans.pop()
                ans.append([newx + a // 2, newy - a // 2])
            on_top = True
print(len(ans))
for x, y in ans:
    if y_lt_x:
        x, y = y, x
    if x_minus:
        x *= -1
    if y_minus:
        y *= -1
    print(x, y)
