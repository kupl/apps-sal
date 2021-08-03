class Solution:

    def maxLength(self, arr: List[str]) -> int:
        arr_sets = [set(x) for x in arr]

        def buildSet(bitlist):
            output = set()
            for i, bit in enumerate(bitlist):
                if bit:
                    output = output.union(arr_sets[i])
            return output

        def recurse(bitlist, index):
            if index == len(arr):
                return len(buildSet(bitlist))

            not_included = recurse(bitlist, index + 1)

            if len(arr_sets[index]) != len(arr[index]) or buildSet(bitlist).intersection(arr_sets[index]):
                return not_included
            else:

                new_bitlist = bitlist[:]
                new_bitlist[index] = 1
                return max(not_included, recurse(new_bitlist, index + 1))

        return recurse([0 for _ in arr], 0)
