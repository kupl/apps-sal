import sys
t = int(input())
for i in range(t):
    remove_from_all = 0
    input()
    (m, k) = (int(x) for x in input().split())
    dishes = [int(x) for x in input().split()]
    inputs = []
    for j in range(m - 1):
        (t, r) = (int(x) for x in input().split())
        inputs.append((t - 1, r))
    seen_upset = False
    for (i, v) in enumerate(inputs):
        (t, r) = v
        if r == 1 and (not seen_upset):
            impossible = set()
            for j in range(i, len(inputs)):
                (_t, _r) = inputs[j]
                impossible.add(_t)
            for j in range(len(dishes)):
                if dishes[j] > remove_from_all:
                    impossible.add(j)
            minimal = float('inf')
            for j in range(len(dishes)):
                if j not in impossible:
                    minimal = min(dishes[j], minimal)
                    dishes[j] = 0
            remove_from_all -= minimal
            seen_upset = True
        if t == -1:
            remove_from_all += 1
        else:
            dishes[t] -= 1
    for j in dishes:
        sys.stdout.write('Y' if j - remove_from_all <= 0 else 'N')
    print('')
