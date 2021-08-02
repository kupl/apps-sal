N = int(input())
S = input()
count = 0
for i in range(N - 2):
    if S[i:i + 3] == "ABC":
        count += 1
print(count)
