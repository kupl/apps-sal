class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {}
        power[1] = 0
        current = {}
        nums = list(range(lo, hi + 1))
        for i in nums:
            self.get_power_value(power, current, i)
        value = sorted(list(current.items()), key=lambda x: x[1])
        arr = list([x[0] for x in value])
        return arr[k - 1]

    def get_power_value(self, power, current, num):
        arr = []
        start = num
        if num in power:
            current[num] = power[num]
        else:
            arr = []
            value = num
            found_power = 0
            while value != 1:
                if value % 2 == 0:
                    value /= 2
                else:
                    value = value * 3 + 1
                arr.append(value)
                if value in power:
                    found_power = power[value]
                    break
            for i in range(0, len(arr)):
                power[start] = len(arr) - i + found_power
                start = arr[i]
            current[num] = power[num]
