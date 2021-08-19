n, m = list(map(int, input().split()))
color = False
for _ in range(n):
    l = input()
    for c in ['C', 'M', 'Y']:
        if c in l:
            color = True
print('#Color' if color else '#Black&White')
