(h, w) = list(map(int, input().split()))
print('#' * (w + 2))
for i in range(h):
    data = list(map(str, input().split()))
    data2 = ['#'] + data + ['#']
    print(''.join(data2))
print('#' * (w + 2))
