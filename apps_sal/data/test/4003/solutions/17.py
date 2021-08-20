n = int(input())
nums = list(map(int, input().split()))


def foo(l, r, prev=0):
    ans = ''
    while l <= r:
        if nums[l] <= prev and nums[r] <= prev:
            break
        if prev < nums[l] < nums[r]:
            ans += 'L'
            prev = nums[l]
            l += 1
        elif prev < nums[r] < nums[l]:
            ans += 'R'
            prev = nums[r]
            r -= 1
        elif nums[r] > nums[l]:
            ans += 'R'
            prev = nums[r]
            r -= 1
        elif nums[r] < nums[l]:
            ans += 'L'
            prev = nums[l]
            l += 1
        elif l == r:
            ans += 'R'
            break
        else:
            a1 = 'L' + foo(l + 1, r, nums[l])
            a2 = 'R' + foo(l, r - 1, nums[l])
            ans += a1 if len(a1) > len(a2) else a2
            break
    return ans


ans = foo(0, n - 1)
print(len(ans))
print(ans)
