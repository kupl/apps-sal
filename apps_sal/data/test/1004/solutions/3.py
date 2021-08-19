n = int(input())
a = list(map(int, input().split()))
(ans, q1, naw, q2) = ([], -1, {}, 0)
for q in range(len(a)):
    if a[q] < 0 and -a[q] not in naw:
        print(-1)
        break
    elif a[q] < 0:
        naw[-a[q]] -= 1
        q2 -= 1
        if naw[-a[q]] < 0:
            print(-1)
            break
    elif a[q] in naw:
        print(-1)
        break
    else:
        naw[a[q]] = 1
        q2 += 1
    if q2 == 0:
        naw = {}
        ans.append(q - q1)
        q1 = q
else:
    if q2 == 0:
        print(len(ans))
        print(*ans)
    else:
        print(-1)
