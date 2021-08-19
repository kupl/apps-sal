class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        l = len(A)
        rem = l % K
        # find indexes where the number changes
        # add to change_list based on remainder class mod K
        prev = 1
        change_list = [[] for i in range(K)]
        for ind, num in enumerate(A):
            if prev != num:
                prev = num
                change_list[ind % K].append(ind)
        if num == 0:
            change_list[rem].append(l)

        num_flips = 0

        for r, mini_list in enumerate(change_list):
            mini_list_len = len(mini_list)
            if mini_list_len % 2 == 1:
                return -1
            for i in range(mini_list_len // 2):
                first = mini_list.pop(0)
                second = mini_list.pop(0)
                num_flips += (second - first) // K

        return num_flips

    def oldMinKBitFlips(self, A: List[int], K: int) -> int:
        l = len(A)

        # find indexes where the number changes
        prev = 1
        change_list = []
        for ind, num in enumerate(A):
            if prev != num:
                prev = num
                change_list.append(ind)

        if len(change_list) == 0:
            return 0

        num_flips = 0

        while len(change_list) > 1:
            first = change_list[0]
            # if first + K > l, we are doomed
            if first + K >= l:
                return -1
            # remove first, and either
                # 1) remove first + K if it exists, or
                # 2) add first + K if it does not exist
            change_list = change_list[1:]
            left_insertion_pt = bisect.bisect_left(change_list, first + K)
            if left_insertion_pt >= len(change_list):
                change_list.append(first + K)
            elif change_list[left_insertion_pt] == first + K:
                del change_list[left_insertion_pt]
            else:
                change_list.insert(left_insertion_pt, first + K)
            num_flips += 1

        if len(change_list) > 0:
            # in this section, len(change_list) == 1
            first = change_list[0]
            q, r = divmod(l - first, K)
            if r == 0:
                return num_flips + q
            else:
                return -1

        return num_flips
