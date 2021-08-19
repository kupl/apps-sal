class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        mem = {}
        for i in arr:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        sorted_array = sorted(list(mem.values()), reverse=True)
        counter = 0
        res = 0
        print(sorted_array)
        for i in sorted_array:
            res += i
            counter += 1
            print(res)
            if res >= len(arr) / 2:
                return counter
