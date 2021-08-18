class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        state2nums = defaultdict(Counter)
        digits.sort(reverse=True)
        for num in digits:
            delta = num % 3
            nstate = defaultdict(Counter)

            for i in range(3):
                if sum(v for k, v in list(state2nums[i].items())) == 0 and i != 0:
                    continue
                target = (delta + i) % 3

                if sum(v for k, v in list(state2nums[target].items())) < sum(v for k, v in list(state2nums[i].items())) + 1:
                    counter = Counter(state2nums[i])
                    counter[num] += 1
                    nstate[target] = counter

            for i in range(3):
                if i in nstate:
                    state2nums[i] = nstate[i]
        print(state2nums)
        nums = sorted([k for k, v in list(state2nums[0].items()) for _ in range(v)], reverse=True)
        ret = ''.join(map(str, nums))
        return '0' if ret and ret[0] == '0' else ret
