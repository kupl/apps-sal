(h, w) = list(map(int, input().split()))
a = [input() for x in range(h)]
print('#' * (w + 2))
for s in a:
    print('#' + s + '#')
print('#' * (w + 2))
