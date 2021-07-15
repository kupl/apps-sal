def main():
    (n, s, t) = list(map(int, input().split(' ')))
    s -= 1
    t -= 1
    if s == t:
        return 0
    nums = list([int(i) - 1 for i in input().split(' ')])
    slow = s
    fast = nums[slow]
    i = 0
    while slow != t:
        if slow == fast:
            i = -1
            break
        slow = nums[slow]
        fast = nums[nums[fast]]
        i += 1
    return i

print(main())

