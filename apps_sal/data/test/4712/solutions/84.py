(H, W) = map(int, input().split())
scr_list = [input() for _ in range(H)]
print('#' * (W + 2))
for i in scr_list:
    print('#' + i + '#')
print('#' * (W + 2))
