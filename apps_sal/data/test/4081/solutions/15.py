n = int(input())
arr = list(map(int, input().strip().split()))
fl = 1
ans = ''
c = 0
st = 0
en = n - 1
la = 0
while fl:
    if st >= n or en <= -1:
        break
    if arr[st] > la:
        if arr[en] > la:
            if arr[en] > arr[st]:
                st += 1
                la = arr[st - 1]
                ans += 'L'
                c += 1
            else:
                en -= 1
                la = arr[en + 1]
                ans += 'R'
                c += 1
        else:
            st += 1
            la = arr[st - 1]
            ans += 'L'
            c += 1
    elif arr[en] > la:
        en -= 1
        la = arr[en + 1]
        ans += 'R'
        c += 1
    else:
        break
print(c)
print(ans)
