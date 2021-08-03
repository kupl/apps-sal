class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(position, m, target):
            ct = 1
            j = 0
            k = 1
            flag = False
            while k < len(position) and ct < m:
                if position[k] - position[j] >= target:
                    ct += 1
                    if not flag:
                        kk = k
                        flag = True
                    j = k
                k += 1
            return (ct == m), kk

        position = sorted(position)
        max_p = position[-1]
        i = position[0]
        if m == 2:
            return max_p - i
        else:
            target = (max_p - i) // (m - 1)
            ct = 1
            b, kk = check(position, m, target)
            if not b:
                while not b and kk != 1:
                    target = position[kk] - i
                    target2 = position[kk - 1] - i
                    b, kk = check(position, m, target2)
                if not b:
                    left = 1
                else:
                    left = position[kk] - i
                right = target
                while left + 1 < right:
                    target = (left + right) // 2
                    if check(position, m, target)[0]:
                        left = target
                    else:
                        right = target
                target = left

            return target
