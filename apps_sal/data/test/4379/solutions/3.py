n = int(input())
s = list(map(int, input().split()))
rl = {}
best_range = range(0)
for x in s:
    run = rl[x] = rl.get(x - 1, 0) + 1
    r = range(x - run + 1, x + 1)
    if len(r) > len(best_range):
        best_range = r
res = list(best_range)
size = len(res)
output = []
pointer = 0
for (i, c) in enumerate(s):
    if res[pointer] == c:
        output.append(str(i + 1))
        pointer += 1
    if pointer >= size:
        break
print(size)
print(' '.join(output))
