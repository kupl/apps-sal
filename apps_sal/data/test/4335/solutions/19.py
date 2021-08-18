N = int(input())
S = input()

result = "No"
if N % 2 == 0:
    s1 = S[0:N // 2]
    s2 = S[N // 2:N]
    result = "Yes" if s1 == s2 else "No"

print(result)
