import sys
MIN = -1000000000
MAX = -MIN


def odds_evens(string):
    f = {}
    for letter in string:
        if letter not in f:
            f[letter] = 0
        f[letter] += 1
    (n_odds, n_evens) = (0, 0)
    for (key, val) in list(f.items()):
        if val % 2 != 0:
            n_odds += 1
        else:
            n_evens += 1
    return (n_odds, n_evens)


string = sys.stdin.readline().strip()
(n_odds, n_evens) = odds_evens(string)
if n_odds == 0:
    print('First')
elif n_odds % 2 == 0:
    print('Second')
else:
    print('First')
