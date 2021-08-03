
n = int(input())

arr = list(map(int, input().strip().split()))

fl = 1

ans = ""
c = 0

st = 0
en = n - 1

la = 0
floop = 0
while fl:
    if st >= n or en <= -1:

        break

    if arr[st] == arr[en]:
        floop = 1
        break

    if arr[st] > la:
        if arr[en] > la:
            if arr[en] > arr[st]:
                st += 1
                la = arr[st - 1]
                ans += "L"
                c += 1
            else:
                en -= 1
                la = arr[en + 1]
                ans += "R"
                c += 1
        else:
            st += 1
            la = arr[st - 1]
            ans += "L"
            c += 1
    else:
        if arr[en] > la:
            en -= 1
            la = arr[en + 1]
            ans += "R"
            c += 1
        else:
            break
# print(floop)
if floop == 1:
    orig = la
    cm = 0
    s1 = ""
    for i in range(st, en + 1):
        if arr[i] > la:
            la = arr[i]
            cm += 1
            s1 += "L"
        else:
            break
    cn = 0
    s2 = ""
    la = orig
    for i in range(en, st - 1, -1):
        if la < arr[i]:
            cn += 1
            s2 += "R"
            la = arr[i]
        else:
            break
    if cn > cm:
        ans += s2
    else:

        ans += s1
    c += max(cn, cm)
    # print(s1,s2)


print(c)
print(ans)
