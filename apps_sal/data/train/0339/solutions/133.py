class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()

        def f(n):
            if n == 2 or n == 1:
                return 1
            return f(n - 1) + n - 1

        def yanzheng(a, num):
            '''
            接受一个数字a和一个有序列表num
            用动态规划算法验证是否存在num[i] * num[j] == a*a'''

            a = a * a
            head = 0
            end = len(num) - 1
            count = 0
            while True:
                headlen = 1
                endlen = 1
                if head >= end:
                    return count
                if num[head] * num[end] > a:
                    end -= 1
                elif num[head] * num[end] < a:
                    head += 1
                elif num[head] * num[end] == a:
                    if num[head] == num[end]:
                        count += f(end - head + 1)
                        head = end
                    elif num[head] == num[head + 1] or num[end] == num[end - 1]:
                        while num[head] == num[head + headlen]:
                            headlen += 1
                        while num[end] == num[end - endlen]:
                            endlen += 1
                        count += headlen * endlen
                        head += headlen
                        end -= endlen
                    else:
                        count += 1
                        end -= 1

        count = 0
        for i in nums1:
            count += yanzheng(i, nums2)
        for i in nums2:
            count += yanzheng(i, nums1)

        return count
