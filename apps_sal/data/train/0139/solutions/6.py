class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        L = len(A)
        N = len(A[0])
        sort_groups = [[i for i in range(L)]]
        count = 0

        for i in range(N):

            new_groups = []
            in_order = True

            for group in sort_groups:
                new_group = []
                curr_ord = 0

                for g_idx in group:

                    char = A[g_idx][i]
                    if ord(char) > curr_ord:
                        if curr_ord != 0:
                            new_groups.append(new_group)
                        new_group = [g_idx]
                        curr_ord = ord(char)

                    elif ord(char) == curr_ord:
                        new_group.append(g_idx)

                    else:
                        in_order = False
                        break

                if not in_order:
                    break

                if new_group != []:
                    new_groups.append(new_group)

            if in_order:
                sort_groups = new_groups

            else:
                count += 1

        return count
