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
            # print(\"Bitlist: {a}, Index: {b}\".format(a=bitlist, b=index))
            if index == len(arr):
                # print(\"returning length\")
                return len(buildSet(bitlist))

            new_bitlist = bitlist[:]
            new_bitlist[index] = 0
            # print(\"recursing with not included\")
            not_included = recurse(new_bitlist, index + 1)

            if len(arr_sets[index]) != len(arr[index]) or buildSet(bitlist).intersection(arr_sets[index]):
                return not_included
            else:
                # print(\"return max of both\")

                new_bitlist[index] = 1
                return max(not_included, recurse(new_bitlist, index + 1))

        return recurse([0 for _ in arr], 0)

        # [0, 1, 1, 0]
