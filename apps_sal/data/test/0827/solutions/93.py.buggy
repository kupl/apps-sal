N = int(input())
T = input()
S = '110' * N
if T == '1':
    print(2 * 10**10)
    return

for i in range(3):
    if S[i:N + i] == T:
        print((3 * 10**10 - N - i) // 3 + 1)
        return
print(0)
