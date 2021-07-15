N = int(input())

pairs = []
for i in range(N):
    x, w = list(map(int, input().split()))
    pairs.append((x, w))

sorted_pairs = sorted(pairs, key=lambda x: x[0])

stack = []
stack.append(sorted_pairs[0])
for x, w in sorted_pairs[1:N]:
    right_x, right_w = stack[-1]
    if right_x + right_w <= x - w:
        stack.append((x, w))
    else:
        if x + w < right_x + right_w:
            stack[-1] = (x, w)

print(len(stack))

