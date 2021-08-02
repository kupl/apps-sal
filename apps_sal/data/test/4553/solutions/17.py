import re
A, B = list(map(int, input().split()))
S = input()
n_pattern = "[0-9]"
res = "Yes"
for i in range(A + B + 1):
    if i < A:
        if re.match(n_pattern, S[i]) is None:
            res = "No"
            break
    elif i == A:
        if S[i] != "-":
            res = "No"
            break
    else:
        if re.match(n_pattern, S[i]) is None:
            res = "No"
            break

print(res)
