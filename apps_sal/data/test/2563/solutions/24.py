t = int(input())
for i in range(t):
    nums = list(map(int, list(input())))
    (nums0, nums1) = ([], [])
    for num in nums:
        if num % 2 == 0:
            nums0.append(str(num))
        else:
            nums1.append(str(num))
    nums0.append(str(99))
    nums1.append(str(99))
    (p0, p1) = (0, 0)
    (l0, l1) = (len(nums0) - 1, len(nums1) - 1)
    ans = str()
    while p0 < l0 or p1 < l1:
        p0_prev = p0
        while p0 < l0 and nums0[p0] < nums1[p1]:
            p0 += 1
        ans += ''.join(nums0[p0_prev:p0])
        p1_prev = p1
        while p1 < l1 and nums1[p1] < nums0[p0]:
            p1 += 1
        ans += ''.join(nums1[p1_prev:p1])
    print(ans)
