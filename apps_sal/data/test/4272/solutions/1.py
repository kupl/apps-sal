N = int(input())
S = input()
target = 'ABC'
cnt = 0
for i in range(0, len(S) - 2):
    if S[i:i + 3] == target:
        cnt += 1
print(cnt)
