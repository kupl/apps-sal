import sys

N = int(input())

co = []
x, y = map(int, input().split())
co.append((x, y))
Amod = (x + y) % 2
flag = True
max_co = abs(x) + abs(y)
for i in range(N - 1):
    x, y = map(int, input().split())
    co.append((x, y))

    if(Amod != (x + y) % 2):
        flag = False

    tmp = abs(x) + abs(y)
    max_co = max(max_co, tmp)

if(flag is False):
    print(-1)
    return

ex2 = [1, 2, 4, 8, 16, 32]
expo = 32
# print(maxxy)
while(expo < max_co):
    expo *= 2
    ex2.append(expo)


ans_list = []
for x, y in co:
    if Amod == 0:
        x -= 1
        ans = "R"
    else:
        ans = ""

    for arm in reversed(ex2):
        # print("present", x, y)
        if abs(x) > abs(y):
            if x > 0:
                x -= arm
                ans = "R" + ans
            else:
                x += arm
                ans = "L" + ans
        else:
            if y > 0:
                y -= arm
                ans = "U" + ans
            else:
                y += arm
                ans = "D" + ans
    # print(x, y)

    ans_list.append(ans)

if Amod == 0:
    ex2.append(1)

print(len(ex2))
arm = ""
for a in ex2:
    arm += " " + str(a)
print(arm[1:])
for a in ans_list:
    print(a)
