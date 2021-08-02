s = [*input()]; print('NYoe s'[all([1 if s.count(i) % 2 == 0 else 0 for i in set(s)])::2])
