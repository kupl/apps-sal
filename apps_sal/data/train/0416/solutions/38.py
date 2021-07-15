class Solution:
    def catMouseGame(self, graph):
        TIE                     = 0
        MOUSE_WIN               = 1
        CAT_WIN                 = 2
        MOUSE_TURN              = 'MOUSE'
        CAT_TURN                = 'CAT'
        HOLE_POSITION           = 0
        INITIAL_MOUSE_POSITION  = 1
        INITIAL_CAT_POSITION    = 2

        win_states = {}
        for m_pos, _ in enumerate(graph):
            for c_pos, _ in enumerate(graph):
                for turn in [MOUSE_TURN, CAT_TURN]:
                    key = (m_pos, c_pos, turn)
                    if m_pos == 0 or c_pos == 0:
                        # If the mouse reaches the hole, the mouse wins.
                        # The cat also isn't allowed to go on the node corresponding
                        # to the hole, so mark the cat doing that as also a win.
                        win_states[key] = MOUSE_WIN
                    elif m_pos == c_pos:
                        win_states[key] = CAT_WIN
                    else:
                        win_states[key] = TIE
        for node_id in graph:
            turn = MOUSE_TURN
            for m_pos, _ in enumerate(graph):
                for c_pos, _ in enumerate(graph):
                    all_cat_win = False
                    if win_states[(m_pos, c_pos, turn)] == TIE:
                        neighbor_states = [win_states[(node, c_pos, CAT_TURN)] for node in graph[m_pos]]
                        if all(win == CAT_WIN for win in neighbor_states):
                            win_states[(m_pos, c_pos, turn)] = CAT_WIN
                        elif any(win == MOUSE_WIN for win in neighbor_states):
                            win_states[(m_pos, c_pos, turn)] = MOUSE_WIN
            turn = CAT_TURN
            for m_pos, _ in enumerate(graph):
                for c_pos, _ in enumerate(graph):
                    if win_states[(m_pos, c_pos, turn)] == TIE:
                        neighbor_states = [win_states[(m_pos, node, MOUSE_TURN)] for node in graph[c_pos]]
                        if all(win == MOUSE_WIN for win in neighbor_states):
                            win_states[(m_pos, c_pos, turn)] = MOUSE_WIN
                        elif any(win == CAT_WIN for win in neighbor_states):
                            win_states[(m_pos, c_pos, turn)] = CAT_WIN

        return win_states[(1, 2, MOUSE_TURN)]

