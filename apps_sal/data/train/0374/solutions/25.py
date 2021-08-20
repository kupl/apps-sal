class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:

        def save(w1, w2):
            n = len(w1)
            for i in range(n):
                if w1[i:] == w2[:n - i]:
                    return n - i
            return 0
        N = len(A)
        s = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    s[i][j] = save(A[i], A[j])
        end_state = (1 << N) - 1
        import functools

        @functools.lru_cache(None)
        def DFS(cur_state, cur_pos):
            if cur_state == end_state:
                return (0, [cur_pos])
            cur_save = -100
            pre_pos = 0
            for pre_pos in range(N):
                if pre_pos == 0:
                    pre_pos_b = 1
                else:
                    pre_pos_b = pre_pos_b << 1
                if pre_pos_b | cur_state == cur_state:
                    continue
                if cur_save < s[pre_pos][cur_pos] + DFS(cur_state | pre_pos_b, pre_pos)[0]:
                    cur_save = s[pre_pos][cur_pos] + DFS(cur_state | pre_pos_b, pre_pos)[0]
                    path = DFS(cur_state | pre_pos_b, pre_pos)[1] + [cur_pos]
            return (cur_save, path)
        ss = -1
        pp = []
        for last_pos in range(N):
            if not last_pos:
                last_pos_b = 1
            else:
                last_pos_b = last_pos_b << 1
            if ss < DFS(last_pos_b, last_pos)[0]:
                (ss, pp) = DFS(last_pos_b, last_pos)
        res = A[pp[0]]
        for i in range(1, N):
            res += A[pp[i]][s[pp[i - 1]][pp[i]]:]
        return res
