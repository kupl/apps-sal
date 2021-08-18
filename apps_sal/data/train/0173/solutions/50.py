class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        modFrequencies = {}
        for i in range(0, len(arr)):
            difference = arr[i] % k
            if difference not in modFrequencies:
                modFrequencies[difference] = 0
            modFrequencies[difference] += 1

        for mod in modFrequencies:
            if mod == 0:
                if modFrequencies[mod] % 2 == 1:
                    return False
            elif k - mod not in modFrequencies or modFrequencies[mod] != modFrequencies[k - mod]:
                return False
        return True
