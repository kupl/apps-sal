class Player:
    __slots__ = ['choices']

    def __init__(self, choices):
        self.choices = choices

    def choose_next(self, row, col):
        return self.choices[row - 1][col - 1]

    def round_score(own, other):
        if own == other + 1 or (own == 1 and other == 3):
            return 1
        return 0


class State:
    __slots__ = ['score_a', 'score_b', 'time']

    def __init__(self, a, b, time):
        self.score_a = a
        self.score_b = b
        self.time = time


def read_player():
    choices = [list(map(int, input().split())) for i in range(3)]
    return Player(choices)


def play(rounds, pa, a, pb, b):
    memo = {}
    score = [0, 0]
    cacat = False

    for i in range(rounds):
        pair = (a, b)
        if pair in memo:
            cycle_len = (i - memo[pair].time)
            cycles = (rounds - i) // cycle_len

            score_a = score[0] - memo[pair].score_a
            score_b = score[1] - memo[pair].score_b

            score[0] += score_a * cycles
            score[1] += score_b * cycles
            rounds -= i + cycles * cycle_len
            cacat = True
            break
        else:
            memo[pair] = State(score[0], score[1], i)

        score[0] += Player.round_score(a, b)
        score[1] += Player.round_score(b, a)
        a, b = pa.choose_next(a, b), pb.choose_next(a, b)

    if cacat:
        for i in range(rounds):
            score[0] += Player.round_score(a, b)
            score[1] += Player.round_score(b, a)
            a, b = pa.choose_next(a, b), pb.choose_next(a, b)

    return score


def main():
    rounds, a, b = list(map(int, input().split()))
    pa = read_player()
    pb = read_player()

    score = play(rounds, pa, a, pb, b)
    print(score[0], score[1])


main()
