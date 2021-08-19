class Solution:
    def tallestBillboard(self, rods):
        sums_lookup = {0: 0}  # current sum is zero, length of left rod is 0
        for rod in rods:
            cur = collections.defaultdict(int)
            # consider 3 cases. Rod is aded to the left bucket, rod is added to the right
            # bucket rod is discarded. In all three cases, update length of the left support
            # beam, however, if new sum already exists, make sure we keep the one
            # with longest left support.
            for current_sum, left_support_length in sums_lookup.items():
                # add rod to the left bucket. Sum will increase since left bucket is
                # represented by positive numbers. Left support beam is longer now
                cur[current_sum + rod] = max(left_support_length + rod, cur[current_sum + rod])
                # add rod to the right bucket. Sum will decrease since right bucket is
                # represented by negative numbers. Left support beam is unchanged.
                cur[current_sum - rod] = max(left_support_length, cur[current_sum - rod])
                # discard rod. Sum and left support beam is unchanged
                cur[current_sum] = max(left_support_length, cur[current_sum])
            sums_lookup = cur
        # our goal is to find sum of all elements in the representation array,
        # that adds up to 0, meaning sum of positivel rods (left bucket) is equal to
        # sum of all negative rods (right bucket)
        return sums_lookup[0]
