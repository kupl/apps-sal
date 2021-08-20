from sys import stdin, stdout
input = stdin.readline
(n, m) = list(map(int, input().split()))
(K, M) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
stdout.write('YES' if a[K - 1] < b[-M] else 'NO')
