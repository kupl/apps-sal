N = int(input())
S = input()
result = 'No'
if N % 2 == 0:
    s1 = S[0:N // 2 - 1]
    s2 = S[N // 2:N - 1]
    if N == 2:
        s1 = S[0:1]
        s2 = S[1:2]
    result = 'Yes' if s1 == s2 else 'No'
print(result)
