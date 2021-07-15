# -*- coding: utf-8 -*-
"""
@Project : CodeForces
@File    : 32.py 
@Time    : 2019/4/26 23:43
@Author  : Koushiro 
"""

def __starting_point():
    n = int(input())
    nums = list(map(int, input().split()))
    result = []
    last = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] < nums[right]:
            if nums[left] > last:
                last = nums[left]
                left += 1
                result.append('L')
            elif nums[right] > last:
                last = nums[right]
                right -= 1
                result.append('R')
            else:
                break
        elif nums[left] > nums[right]:
            if nums[right] > last:
                last = nums[right]
                right -= 1
                result.append('R')
            elif nums[left] > last:
                last = nums[left]
                left += 1
                result.append('L')
            else:
                break
        elif nums[left] == nums[right]:
            l_n = left
            r_n = right
            l_c = 0
            r_c = 0
            l_last = last
            r_last = last
            while l_n <= right:
                if nums[l_n] > l_last:
                    l_c += 1
                    l_last = nums[l_n]
                    l_n += 1
                else:
                    break
            while r_n >= left:
                if nums[r_n] > r_last:
                    r_c += 1
                    r_last = nums[r_n]
                    r_n -= 1
                else:
                    break
            if l_c > r_c:
                for i in range(l_c):
                    result.append("L")
            else:
                for i in range(r_c):
                    result.append("R")
            break

    print(len(result))
    print("".join(result))

__starting_point()
