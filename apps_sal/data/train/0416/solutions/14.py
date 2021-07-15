TIE        = 0
MOUSE_WIN  = 1
CAT_WIN    = 2
MOUSE_TURN = 'MOUSE'
CAT_TURN   = 'CAT'
GOAL       = 0
MPOS_INIT  = 1
CPOS_INIT  = 2

class Solution:
  def catMouseGame(self, graph):
    win_states = {}
    for mpos, _ in enumerate(graph):
      for cpos, _ in enumerate(graph):
        for turn in [MOUSE_TURN, CAT_TURN]:
          key = (mpos, cpos, turn)
          if mpos == GOAL:   win_states[key] = MOUSE_WIN
          elif mpos == cpos: win_states[key] = CAT_WIN
          else:              win_states[key] = TIE
    while True:
      changes = 0
      turn = MOUSE_TURN
      for mpos, adj in enumerate(graph):
        for cpos, _ in enumerate(graph):
          all_cat_win = False
          if win_states[(mpos, cpos, turn)] == TIE:
            adj_wins = [win_states[(node, cpos, CAT_TURN)] for node in adj]
            if all(win == CAT_WIN for win in adj_wins):
              win_states[(mpos, cpos, turn)], changes = CAT_WIN, changes + 1
            elif any(win == MOUSE_WIN for win in adj_wins):
              win_states[(mpos, cpos, turn)], changes = MOUSE_WIN, changes + 1
      turn = CAT_TURN
      for mpos, _ in enumerate(graph):
        for cpos, adj in enumerate(graph):
          if win_states[(mpos, cpos, turn)] == TIE:
            adj_wins = [win_states[(mpos, node, MOUSE_TURN)] for node in adj if node != GOAL]
            if all(win == MOUSE_WIN for win in adj_wins):
              win_states[(mpos, cpos, turn)], changes = MOUSE_WIN, changes + 1
            elif any(win == CAT_WIN for win in adj_wins):
              win_states[(mpos, cpos, turn)], changes = CAT_WIN, changes + 1
      if changes == 0:
        break
    return win_states[(MPOS_INIT, CPOS_INIT, MOUSE_TURN)]

