k = int(input())
A = [input().strip() for i in range(4)]
cnt = [0 for i in range(10)]
flag = False
for y in range(4):
    if flag:
        break
    for x in range(4):
        c = A[y][x]
        if c == '.':
            continue
        cnt[int(c)] += 1
        if cnt[int(c)] > 2 * k:
            print("NO")
            flag = True
            break

if not(flag):
    print("YES")

