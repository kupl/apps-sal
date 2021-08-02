st = input()
k = int(input())
w = list(map(int, input().split()))
w2 = {chr(ord('a') + i): w[i] for i in range(26)}
m = max(w)
print(sum([w2[st[i]] * (i + 1) for i in range(len(st))]) + sum([i * m for i in range(len(st) + 1, len(st) + 1 + k)]))
