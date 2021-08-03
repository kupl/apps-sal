from sys import stdin, exit
input = stdin.readline


def i(): return input()
def ii(): return int(input())
def iis(): return list(map(int, input().split()))
def liis(): return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


t = ii()
for _ in range(t):
    time = 0
    x, y = 0, 0
    visited = set()
    s = input()
    for i in s:
        old_x = x
        old_y = y
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'E':
            x += 1
        elif i == 'W':
            x -= 1
        else:
            continue
        if (old_x, old_y, x, y) in visited:
            time += 1
        else:
            time += 5

        visited.add((x, y, old_x, old_y))
        visited.add((old_x, old_y, x, y))

    print(time)
