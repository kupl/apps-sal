(h, w) = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())
print('#' * (w + 2))
for i in range(h):
    print('#' + a[i] + '#')
print('#' * (w + 2))
