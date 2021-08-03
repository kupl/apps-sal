from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n, k = tuple(int(x) for x in stdin.readline().split())
    lst = sorted(int(x) for x in stdin.readline().split())
    print(sum(lst[-k - 1:]))
