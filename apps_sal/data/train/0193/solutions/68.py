class Solution:
    def floor_counter(self, n):
        if n % 2 == 0:
            return n / 2
        else:
            return (n + 1) / 2

    def minSetSize(self, arr: List[int]) -> int:
        ceiling = self.floor_counter(len(arr))
        freq = {}
        for elem in arr:
            if elem in freq:
                freq[elem] += 1
            else:
                freq[elem] = 1
        sorted_freq = sorted(freq.items(), key=lambda k: k[1], reverse=True)
        sum = 0
        type_counter = []
        for i in range(len(sorted_freq)):
            sum += (sorted_freq[i][1])
            print(sum)
            type_counter.append(sorted_freq[i][0])
            if sum >= ceiling:
                return len(type_counter)
