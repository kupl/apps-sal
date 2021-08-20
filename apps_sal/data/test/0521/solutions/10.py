N = int(input())
S = input()
if N == 1:
    if S == '?':
        print('Yes')
        quit()
    else:
        print('No')
        quit()
for i in range(N - 1):
    char1 = S[i]
    char2 = S[i + 1]
    if char1 == char2 and char1 != '?':
        print('No')
        quit()
if S.count('?') == 0:
    print('No')
    quit()
for i in range(N - 1):
    char1 = S[i]
    char2 = S[i + 1]
    if char1 == char2:
        print('Yes')
        quit()
if S[0] == '?' or S[N - 1] == '?':
    print('Yes')
    quit()
for i in range(1, N - 1):
    if S[i] == '?' and S[i - 1] == S[i + 1]:
        print('Yes')
        quit()
print('No')
