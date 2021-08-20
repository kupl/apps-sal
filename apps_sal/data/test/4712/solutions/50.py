(h, w) = map(int, input().split())
a = [input() for _ in range(h)]
print('#' * (w + 2))
for i in range(h):
    print('#' + a[i] + '#')
print('#' * (w + 2))
