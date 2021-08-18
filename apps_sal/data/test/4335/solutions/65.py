N = int(input())
S = input()

result = 'No'

if len(S) % 2 == 0:
    if S[:len(S) // 2] == S[len(S) // 2:]:
        result = 'Yes'

print(result)
