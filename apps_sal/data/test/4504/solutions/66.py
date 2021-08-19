S = input()
odd = len(S) % 2
little = odd + (1 - odd) * 2
start = len(S) - 1 - little
ans = 0
for i in range(start, 0, -2):
    half = (i + 1) // 2
    a = S[:half]
    b = S[half:half * 2]
    if a == b:
        ans = len(a) * 2
        break
print(ans)
