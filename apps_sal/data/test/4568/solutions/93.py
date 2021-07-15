N = int(input())
S = input()

ss = []
for s in S:
    if s not in ss:
        ss.append(s)

max_count = 0
for i in range(1, N-1):
    count = 0
    for s in ss:
        x = S[0:i]
        y = S[i:N]
        if s in x and s in y:
            count += 1
    if count > max_count:
        max_count = count

print(max_count)
