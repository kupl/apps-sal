from sys import stdin, stdout
n, n1, n2 = map(int, stdin.readline().split())
numbers = sorted(list(map(int, stdin.readline().split())))[::-1][:n1 + n2][::-1]


ans = 0
if n1 > n2:
    ans += sum(numbers[:n1]) / n1 + sum(numbers[::-1][:n2]) / n2
else:
    ans += sum(numbers[:n2]) / n2 + sum(numbers[::-1][:n1]) / n1

stdout.write(str(ans))
