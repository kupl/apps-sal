H, W = map(int, input().split())
print('#' * (W + 2) ) # head
for _ in range(H):
  print('#', input(), '#', sep='')

print('#' * (W + 2) ) # tail
