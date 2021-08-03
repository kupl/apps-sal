from sys import stdin, exit

n, m = list(int(x) for x in stdin.readline().split())
for _ in range(n):
    line = stdin.readline().split()
    for c in line:
        if c in 'CMY':
            print('#Color')
            return
print('#Black&White')
