from sys import stdin


def volume_of(s):
    count = 0
    for c in s:
        count += 1 if c.isupper() else 0
    return count


n = int(stdin.readline())
data = stdin.readline().rstrip().split()
print(max(list(map(volume_of, data))))
