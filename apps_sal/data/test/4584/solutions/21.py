n = {i + 1: 0 for i in range(int(input()))}
for i in map(int, input().split()): n[i] += 1
[print(i) for i in n.values()]
