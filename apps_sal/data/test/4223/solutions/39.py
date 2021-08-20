N = int(input())
S = str(input())
count = 1
for i in range(N - 1):
    if S[i] != S[i + 1]:
        count += 1
print(count)
