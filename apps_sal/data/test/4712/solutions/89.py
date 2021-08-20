(H, W) = list(map(int, input().split()))
A = [list(input()) for _ in range(H)]
print('#' * (W + 2))
for a in A:
    print('#' + ''.join(a) + '#')
print('#' * (W + 2))
