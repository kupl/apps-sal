class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = defaultdict(int)
        for num in arr:
            frequency[num] += 1
        arrLength = len(arr)
        pairs = []
        for key, val in frequency.items():
            pairs.append((val, key))
        pairs.sort(reverse=True)
        cumSum = 0
        for counter, pair in enumerate(pairs):
            frequency, key = pair
            cumSum += frequency
            if cumSum >= arrLength / 2:
                return counter + 1
