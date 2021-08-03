h, w = map(int, input().split())
huta = ['#' for _ in range(w + 2)]
huta = ''.join(huta)
print(huta)
for _ in range(h):
    a = input()
    print('#{}#'.format(a))
print(huta)
