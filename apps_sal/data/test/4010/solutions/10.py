t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [[] for i in range(n + 2)]
    for i in range(n):
        cnt[arr[i]].append(i)
    for el in cnt:
        if len(el) > 2:
            print("YES")
            break
        if (len(el) < 2):
            continue
        if abs(el[1] - el[0]) != 1:
            print("YES")
            break
    else:
        print("NO")

