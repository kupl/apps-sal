S = input()
T = input()
max_count = 0
for i in range(len(S)-len(T)+1):
    s = S[i:i+len(T)]
    count = 0
    for j in range(len(T)):
        if s[j] == T[j]:
            count = count + 1
    if max_count <= count:
        max_count = count
        ans = len(T) - count
print(ans)

