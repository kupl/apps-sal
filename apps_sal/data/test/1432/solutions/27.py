n = int(input())
inp = list(map(int, input().split()))
inp = [2 * item for item in inp]
s = 0
for i in range(1, len(inp)):
    if i % 2 == 1:
        s -= inp[i]
    else:
        s += inp[i]
ans = [(s + inp[0]) // 2]
for i in range(len(inp) - 1):
    ans.append(inp[i] - ans[-1])
for item in ans:
    print(item, end=" ")
