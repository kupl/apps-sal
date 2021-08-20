def compare(s1, t1):
    count = 0
    for (a, b) in zip(s1, t1):
        if a != b:
            count += 1
    return count


s = input()
t = input()
ans = 1001
for i in range(len(s) - len(t) + 1):
    ret = compare(s[i:], t)
    ans = min(ret, ans)
print(ans)
