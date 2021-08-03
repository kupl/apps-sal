class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        freq = []
        k = 0
        while k < len(arr):
            j = k + 1
            fr = 1
            while j < len(arr):
                if arr[j] == arr[k]:
                    fr += 1
                else:
                    break
                j += 1
                k += 1
            freq.append(fr)
            k += 1
        freq.sort()
        freq.reverse()
        k = 0
        no = 0
        count = 0
        while k < len(freq) and count < len(arr) / 2:
            if freq[0] >= len(arr) / 2:
                no += 1
                break
            count = count + freq[k]
            no += 1
            k += 1
        return no
