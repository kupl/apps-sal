S = input()
arr = []
seq = 1
for (i, (a, b)) in enumerate(zip(S, S[1:])):
    if a == b:
        seq += 1
    else:
        arr.append(seq)
        seq = 1
arr.append(seq)
assert len(arr) % 2 == 0
ans = [0] * len(S)
i = 0
for (r, l) in zip(arr[::2], arr[1::2]):
    i += r
    ans[i - 1] = ans[i] = (r + l) // 2
    if (r + l) % 2:
        if r < l:
            if l % 2:
                ans[i] += 1
            else:
                ans[i - 1] += 1
        elif r % 2:
            ans[i - 1] += 1
        else:
            ans[i] += 1
    i += l
print(*ans)
