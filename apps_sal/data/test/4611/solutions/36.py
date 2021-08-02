#!/user/bin/env pypy3
import sys
from typing import NamedTuple, List


def fast_input():
    return sys.stdin.readline()[:-1]


class Position(NamedTuple):
    t: int
    x: int
    y: int

    def _calc_diff_move(self, position) -> int:
        diff_x = self.x - position.x
        diff_y = self.y - position.y
        return abs(diff_x) + abs(diff_y)

    def can_move_from(self, prev) -> bool:
        diff_t = self.t - prev.t
        diff_move = self._calc_diff_move(prev)
        if not diff_t % 2 == diff_move % 2:
            return False
        return diff_t >= diff_move


def result_format(b: bool) -> str:
    return "Yes" if b else "No"


def solve(positions: List[Position]) -> bool:
    positions = [Position(t=0, x=0, y=0)] + positions
    for p_ind in range(len(positions) - 1):
        p_curr = positions[p_ind]
        p_next = positions[p_ind + 1]
        if not p_next.can_move_from(p_curr):
            return False
    return True


def main():
    n = int(fast_input())
    positions = []
    for _ in range(n):
        t, x, y = list(map(int, fast_input().split()))
        positions.append(Position(t=t, x=x, y=y))
    result = solve(positions)
    print((result_format(result)))


main()
