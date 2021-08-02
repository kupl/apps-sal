import sys
input = sys.stdin.readline

q = int(input())

for testcases in range(q):
    a, b = list(map(int, input().split()))
    S = input().strip()
    S += "X"

    T = []

    NOW = 0
    for s in S:
        if s == ".":
            NOW += 1
        else:
            if NOW != 0:
                T.append(NOW)
            NOW = 0

    count = 0
    noflag = 0
    other = []

    for t in T:
        if b <= t < a:
            noflag = 1
            break
        if a <= t < 2 * b:
            count += 1
        elif t >= 2 * b:
            other.append(t)

    if len(other) >= 2:
        noflag = 1

    if noflag == 1:
        print("NO")
        continue
    if len(other) == 0:
        if count % 2 == 1:
            print("YES")
        else:
            print("NO")
        continue

    OTHER = other[0]

    for left in range(OTHER - a + 1):
        right = OTHER - a - left

        if left >= 2 * b or right >= 2 * b or b <= left < a or b <= right < a:
            continue

        count2 = count

        if left >= a:
            count2 += 1
        if right >= a:
            count2 += 1

        if count2 % 2 == 0:
            print("YES")
            break

    else:
        print("NO")
