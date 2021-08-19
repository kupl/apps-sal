S = input()
mid = len(S) // 2
count = 0
for i in range(mid):
    if S[i] != S[len(S) - 1 - i]:
        count += 1
print(count)
