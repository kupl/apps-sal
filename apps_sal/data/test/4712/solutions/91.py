with open(0) as f:
    (H, W, *a) = f.read().split()
W = int(W)
a.insert(0, '#' * W)
a.append('#' * W)
for x in a:
    print('#' + x.rstrip('\n') + '#')
