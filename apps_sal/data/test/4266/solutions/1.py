import sys
pin = sys.stdin.readline
pout = sys.stdout.write
(K, X) = map(int, pin().split())
for i in range(X - K + 1, X + K):
    pout(f'{i} ')
print()
