c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

f = 0
for a1 in range(min(c1) + 1):
    b1 = c1[0] - a1
    b2 = c1[1] - a1
    b3 = c1[2] - a1

    a2_1 = c2[0] - b1
    a2_2 = c2[1] - b2
    a2_3 = c2[2] - b3
    if not (a2_1 == a2_2 and a2_2 == a2_3):
        continue

    a3_1 = c3[0] - b1
    a3_2 = c3[1] - b2
    a3_3 = c3[2] - b3
    if not (a3_1 == a3_2 and a3_2 == a3_3):
        continue

    print("Yes")
    f = 1
    break

if not f:
    print("No")
