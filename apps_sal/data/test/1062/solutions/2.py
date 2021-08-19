import unittest


def solve(S, T):
    pos_s = {}
    pos_t = {}
    wrongs = []
    distance = 0

    for i, (s, t) in enumerate(zip(S, T)):
        if s != t:
            pos_t[(s, t)] = i
            pos_s[s] = i
            wrongs.append((s, t, i))
            distance += 1

    for wrong, need, i in wrongs:
        j = pos_t.get((need, wrong))
        if j is not None:
            return (distance - 2, i + 1, j + 1)

    for wrong, need, i in wrongs:
        if need in pos_s:
            return (distance - 1, i + 1, pos_s[need] + 1)

    return distance, -1, -1


class Test_solution(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solve("pergament", "permanent"), (1, 4, 6))
        self.assertEqual(solve("wookie", "cookie"), (1, -1, -1))
        self.assertEqual(solve("petr", "egor"), (2, 1, 2))
        self.assertEqual(solve("double", "bundle"), (2, 1, 4))
        self.assertEqual(solve("", ""), (0, -1, -1))


def __starting_point():
    # unittest.main()
    input()
    S = input()
    T = input()
    distance, i, j = solve(S, T)
    print(distance)
    print(i, j)


__starting_point()
