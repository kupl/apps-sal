class Solution:

    def totalFruit(self, tree) -> int:
        if len(tree) < 3:
            return len(tree)
        seq_len = [[tree[0], 0]]
        for f in tree:
            if seq_len[-1][0] == f:
                seq_len[-1][1] += 1
            else:
                seq_len.append([f, 1])
        most = seq_len[0][1]
        if len(seq_len) > 1:
            curr_two_types = set([seq_len[0][0], seq_len[1][0]])
            most = curr_most = seq_len[0][1] + seq_len[1][1]
            for i in range(2, len(seq_len)):
                if seq_len[i][0] in curr_two_types:
                    curr_most += seq_len[i][1]
                else:
                    curr_most = seq_len[i][1] + seq_len[i - 1][1]
                    curr_two_types = set([seq_len[i][0], seq_len[i - 1][0]])
                most = max(most, curr_most)
        return most
