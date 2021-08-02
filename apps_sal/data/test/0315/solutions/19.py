from sys import stdin

n, k = list(map(int, stdin.readline().split()))

a = list(map(int, stdin.readline().split()))


def solve(walks: list) -> (int, list):
    new_walks = [0]
    for i in range(1, n):
        s = walks[i] + walks[i - 1] + new_walks[i - 1]
        new_walks.append(max(0, k - s))
    return sum(new_walks), new_walks


def print_result(number, walks):
    print(number)
    print(' '.join(str(a[i] + walks[i]) for i in range(n)))


n1, result1 = solve(a)
n2, result2 = solve(list(reversed(a)))

if n1 <= n2:
    print_result(n1, result1)
else:
    print_result(n2, result2)
