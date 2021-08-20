class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        r_to_nums = {i: list() for i in range(3)}
        for x in digits:
            r = x % 3
            r_to_nums[r].append(x)
        for i in range(3):
            r_to_nums[i].sort()
        counter = collections.Counter()
        for x in digits:
            counter[str(x)] += 1
        r = sum(digits) % 3
        if r == 1:
            if r_to_nums[1]:
                y = str(r_to_nums[1][0])
                counter[y] -= 1
            elif len(r_to_nums[2]) >= 2:
                y = str(r_to_nums[2][0])
                counter[y] -= 1
                y = str(r_to_nums[2][1])
                counter[y] -= 1
            else:
                return ''
        elif r == 2:
            if r_to_nums[2]:
                y = str(r_to_nums[2][0])
                counter[y] -= 1
            elif len(r_to_nums[1]) >= 2:
                y = str(r_to_nums[1][0])
                counter[y] -= 1
                y = str(r_to_nums[1][1])
                counter[y] -= 1
            else:
                return ''
        res = ''
        for x in sorted(counter, reverse=True):
            cnt = counter[x]
            res += x * cnt
        if not res:
            return res
        return str(int(res))
