class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        group_members = {}
        in_group = [-1 for i in range(len(arr))]
        existing_ms = 0
        lastm = -1
        for i, pos in enumerate(arr):
            pos -= 1
            group_at_left = (pos > 0) and (in_group[pos - 1] != -1)
            group_at_right = (pos < len(arr) - 1) and (in_group[pos + 1] != -1)
            len_left = len(group_members[in_group[pos - 1]]) if group_at_left else 0
            len_right = len(group_members[in_group[pos + 1]]) if group_at_right else 0
            if len_left == m:
                existing_ms -= 1
            if len_right == m:
                existing_ms -= 1
            if (not group_at_left) and (not group_at_right):
                in_group[pos] = pos
                group_members[pos] = [pos]
                if m == 1:
                    existing_ms += 1
            elif group_at_left and group_at_right:
                if (len_left + len_right + 1) == m:
                    existing_ms += 1
                merge_group = in_group[pos - 1]
                in_group[pos] = merge_group
                group_members[merge_group].append(pos)
                group_members[merge_group] += group_members[in_group[pos + 1]]
                for pos_right in group_members[in_group[pos + 1]]:
                    in_group[pos_right] = merge_group
            elif group_at_left:
                if (len_left + 1) == m:
                    existing_ms += 1
                merge_group = in_group[pos - 1]
                in_group[pos] = merge_group
                group_members[merge_group].append(pos)
            else:
                if (len_right + 1) == m:
                    existing_ms += 1
                merge_group = in_group[pos + 1]
                in_group[pos] = merge_group
                group_members[merge_group].append(pos)
            if existing_ms > 0:
                lastm = i + 1
        return lastm
