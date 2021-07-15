from collections import defaultdict
from sys import stderr

n = int(input())

friends = defaultdict(lambda: set())

for i in range(n):
    name, _, *numbers = input().split()
    for number in numbers:
        skip_number = False
        for old_number in list(friends[name]):
            if number.endswith(old_number):
                friends[name].remove(old_number)
            elif old_number.endswith(number):
                skip_number = True
        if not skip_number:
            friends[name].add(number)

print(len(friends))
for name in friends:
    print('{} {} {}'.format(name, len(friends[name]), ' '.join(friends[name])))

