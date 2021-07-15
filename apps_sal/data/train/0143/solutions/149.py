class Solution:
    def totalFruit(self, tree) -> int:
        if len(tree) < 3:
            return len(tree)

        # i = 0
        # while i < len(tree) and tree[i] == tree[0]:
        #     i += 1
        # if i == len(tree):
        #     return i
        # most_fruit = i + 1
        # first_type, f_counter = tree[0], i
        # second_type, s_counter = tree[i], 1

        seq_len = [[tree[0], 0]]
        for f in tree:
            if seq_len[-1][0] == f:
                seq_len[-1][1] += 1
            else:
                seq_len.append([f, 1])
        most = curr_most = seq_len[0][1]
        # print(seq_len)
        if len(seq_len) > 1:
            curr_two_types = set([seq_len[0][0], seq_len[1][0]])
            most = curr_most = seq_len[0][1] + seq_len[1][1]
            for i in range(2, len(seq_len)):
                if seq_len[i][0] in curr_two_types:
                    curr_most += seq_len[i][1]
                else:
                    curr_most = seq_len[i][1] + seq_len[i-1][1]
                    curr_two_types = set([seq_len[i][0], seq_len[i-1][0]])
                most = max(most, curr_most)
                # print(\"---\", most)
        return most
