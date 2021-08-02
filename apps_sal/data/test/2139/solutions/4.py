import unittest


def get_max_s(s):
    n = len(s)
    i = 0
    l = 0
    count = 0

    while i < n:
        if s[i:i + 4] == 'bear':
            count += (n - (i + 4) + 1) * (i - l + 1)
            l = i + 1
            i += 4
            continue
        i += 1

    return count


def __starting_point():
    s = input().strip()
    max_s = get_max_s(s)
    print(max_s)


class TestFoo(unittest.TestCase):
    def test_world(self):
        got = get_max_s('bearbtear')
        self.assertEqual(got, 6)

        got = get_max_s('bearaabearc')
        self.assertEqual(got, 20)


__starting_point()
