class Solution:

    def calculate_weight(self, x, y, z, freq):
        if x == y and y == z:
            return freq[x] * (freq[x] - 1) * (freq[x] - 2) / 6
        if x == y:
            return freq[x] * (freq[x] - 1) / 2 * freq[z]
        if x == z:
            return freq[x] * (freq[x] - 1) / 2 * freq[y]
        if y == z:
            return freq[z] * (freq[z] - 1) / 2 * freq[x]
        return freq[x] * freq[y] * freq[z]

    def calculate_freq(self, A):
        freq = {}
        for k in A:
            if k in list(freq.keys()):
                freq[k] += 1
            else:
                freq[k] = 1
        return freq

    def threeSumMulti(self, A: List[int], target: int) -> int:
        freq = self.calculate_freq(A)
        unique_values = list(freq.keys())
        count = 0
        two_sum_combinations = {}
        print(len(A))
        for x in unique_values:
            for y in unique_values:
                maxval = max(x, y)
                minval = min(x, y)
                if x + y not in two_sum_combinations:
                    two_sum_combinations[x + y] = set()
                two_sum_combinations[x + y].add((maxval, minval))
        for z in unique_values:
            if target - z in two_sum_combinations:
                for (x, y) in two_sum_combinations[target - z]:
                    if z <= y:
                        weight = self.calculate_weight(x, y, z, freq)
                        print((x, y, z, weight))
                        count += weight
        return int(count) % (10 ** 9 + 7)
