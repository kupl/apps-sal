n = int(input())
a = list(map(int, input().split()))
ans = []

three = []
two = []
for i in range(n):
    if a[i] == 0:
        continue
    if a[i] == 3:
        if len(three) > 0:
            x = three.pop()
            ans.append((x, i))
            ans.append((i, i))
            three.append(i)
        else:
            ans.append((i, i))
            three.append(i)

    elif a[i] == 2:
        if len(three) > 0:
            x = three.pop()
            ans.append((x, i))
            ans.append((i, i))
            two.append(i)
        else:
            ans.append((i, i))
            two.append(i)

    else:
        if len(three) > 0:
            x = three.pop()
            ans.append((x, i))
            ans.append((i, i))
        elif len(two) > 0:
            x = two.pop()
            ans.append((x, i))
        else:
            ans.append((i, i))

if len(three) > 0 or len(two) > 0:
    print(-1)

else:
    print(len(ans))
    for i, j in ans:
        print(i + 1, j + 1)
