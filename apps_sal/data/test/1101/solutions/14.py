[n, k] = [int(x) for x in input().split()]

room_free = [bool(1-int(x)) for x in input()]

# maintain queue closest before
# maintain queue of closest after

# maintain two pointers (l, r)
# if l == 0 check

closest_before = []
closest_after = []

# note, he needs k+1 rooms

before = -1
for i in range(n):
    if room_free[i]:
        before = i
    closest_before.append(before)

after = 11**8
for i in range(n-1, -1, -1):
    if room_free[i]:
        after = i
    closest_after.append(after)
closest_after.reverse()


l = -1
r = -1
taken = 0
ans = 10**8


while True:
    if taken != k+1:
        r += 1
        if r >= n:
            break
        if room_free[r]:
            taken += 1
    else:
        l += 1
        if room_free[l]:

            mid = int((l+r)/2)
            # print(l, r, mid, closest_after[mid])
            ans = min(ans, closest_after[mid+1] - l, r - closest_before[mid])
            taken -= 1
print(ans)


