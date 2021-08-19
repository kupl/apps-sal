# 577_B

n = int(input())

ln = [int(i) for i in input().split(" ")]

s = 0
m = 0
for i in ln:
    s += i
    m = max(m, i)

if s % 2 == 1:
    print("NO")
else:
    if m <= s / 2:
        print("YES")
    else:
        print("NO")
