from collections import Counter
S = list(input())
S = Counter(S)
if len(S) == 26:
    ans = "None"
else:
    A = [chr(i) for i in range(97, 97+26)]
    for i in A:
        if i in S:
            continue
        ans = i
        break
print(ans)

