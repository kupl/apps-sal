class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        tran_ptr = 0
        maxlist = []

        while True:
            scan_ptr = tran_ptr
            count = 0
            types = []

            while True:
                if tree[scan_ptr] in types:
                    count += 1
                elif len(types) == 0:
                    types.append(tree[scan_ptr])
                    count += 1
                elif len(types) == 1:
                    tran_ptr = scan_ptr
                    types.append(tree[scan_ptr])
                    count += 1
                else:
                    break
                scan_ptr += 1
                if scan_ptr == len(tree):
                    break
            maxlist.append(count)

            if scan_ptr == len(tree):
                break

        return max(maxlist)
