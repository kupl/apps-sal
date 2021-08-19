class Solution:

    def tallestBillboard(self, rods):
        sums_lookup = {0: 0}
        for rod in rods:
            cur = collections.defaultdict(int)
            for (current_sum, left_support_length) in sums_lookup.items():
                cur[current_sum + rod] = max(left_support_length + rod, cur[current_sum + rod])
                cur[current_sum - rod] = max(left_support_length, cur[current_sum - rod])
                cur[current_sum] = max(left_support_length, cur[current_sum])
            sums_lookup = cur
        return sums_lookup[0]
