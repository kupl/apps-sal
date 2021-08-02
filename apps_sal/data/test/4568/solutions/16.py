N = int(input())
S = input()

max_counter = 0
for i in range(1, N - 1):
    x = set(S[0:i])
    y = set(S[i:N])
    if len(x & y) > max_counter:
        max_counter = len(x & y)

print(max_counter)
