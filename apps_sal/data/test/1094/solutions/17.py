import sys
import collections

_ = sys.stdin.readline()  # read count, not needed for us

names = collections.OrderedDict()

while True:
    name = sys.stdin.readline()
    name = name.strip()

    if not name:
        break

    if name not in names:
        names[name] = None

    names.move_to_end(name)

sys.stdout.write('\n'.join(reversed(names)))
