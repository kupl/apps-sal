(h, w) = map(int, input().split())
p = [input() for _ in range(h)]
print('#' * (w + 2))
for s in p:
    print('#' + s + '#')
print('#' * (w + 2))
