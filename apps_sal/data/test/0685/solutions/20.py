(n, s) = map(int, input().split())
mass = list()
arr = list()
past = -1
answer = 0
for i in range(n):
    (l, r) = map(int, input().split())
    mass.append(r - l)
    if past != -1:
        arr.append(l - past)
    past = r
l2 = 0
local = s
q = mass[0] + s
for j in range(n - 1):
    local -= arr[j]
    if local <= 0:
        l2 = j
        break
    q += mass[j + 1]
answer = q
if local <= 0:
    for i in range(1, n):
        local += arr[i - 1]
        q -= mass[i - 1]
        if local > 0:
            local += arr[l2]
            for j in range(l2, n - 1):
                local -= arr[j]
                if local <= 0:
                    break
                l2 += 1
                q += mass[j + 1]
        if q > answer:
            answer = q
        if local > 0:
            break
print(answer)
