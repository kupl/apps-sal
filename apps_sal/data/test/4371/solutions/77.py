def vax(S, num):
    nums = [999]
    index = [i for (i, x) in enumerate(S) if x == str(num) and i <= len(S) - 3]
    for i in index:
        nums.append(abs(753 - int(S[i] + S[i + 1] + S[i + 2])))
    return min(nums)


S = list(input())
ans = 999
for i in range(10):
    ans = min(vax(S, i), ans)
print(ans)
