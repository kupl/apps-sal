class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        counter = defaultdict(int)

        for ele in arr:

            ele %= k

            if counter[k - ele]:
                counter[k - ele] -= 1
            else:
                counter[ele] += 1

        # print(counter)

        if counter[0] % 2:
            return False

        counter[0] = 0
        for k, v in list(counter.items()):
            if v:
                return False

        return True
