def bs(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return 1

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return bs(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return bs(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return 0


n = int(input())
nrp = []
rc = []
for i in range(n):
    p, c = map(int, input().split())
    if c:
        nrp.append(i + 1)
    if not c:
        rc.append(p)
s = []
rc.sort()
for i in nrp:
    if not bs(rc, 0, len(rc) - 1, i):
        s.append(i)
if not s:
    print("-1")
else:
    print(*sorted(s))
