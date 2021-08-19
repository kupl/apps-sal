(A, B) = map(int, input().split())
S = input()
result = 'Yes'
if '-' in S[:A]:
    result = 'No'
if '-' not in S[A]:
    result = 'No'
if '-' in S[A + 1:]:
    result = 'No'
print(result)
