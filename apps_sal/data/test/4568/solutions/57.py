def al_cnt(k,s):
    count = 0
    if 'a' in s[:k] and 'a' in s[k:]:
        count += 1
    if 'b' in s[:k] and 'b' in s[k:]:
        count += 1
    if 'c' in s[:k] and 'c' in s[k:]:
        count += 1
    if 'd' in s[:k] and 'd' in s[k:]:
        count += 1
    if 'e' in s[:k] and 'e' in s[k:]:
        count += 1
    if 'f' in s[:k] and'f' in s[k:]:
        count += 1
    if 'g' in s[:k] and 'g' in s[k:]:
        count += 1
    if 'h' in s[:k] and 'h' in s[k:]:
        count += 1
    if 'i' in s[:k] and 'i' in s[k:]:
        count += 1
    if 'j' in s[:k] and 'j' in s[k:]:
        count += 1
    if 'k' in s[:k] and 'k' in s[k:]:
        count += 1
    if 'l' in s[:k] and 'l' in s[k:]:
        count += 1
    if 'm' in s[:k] and 'm' in s[k:]:
        count += 1
    if 'n' in s[:k] and 'n' in s[k:]:
        count += 1
    if 'o' in s[:k] and 'o' in s[k:]:
        count += 1
    if 'p' in s[:k] and 'p' in s[k:]:
        count += 1
    if 'q' in s[:k] and 'q' in s[k:]:
        count += 1
    if 'r' in s[:k] and 'r' in s[k:]:
        count += 1
    if 's' in s[:k] and 's' in s[k:]:
        count += 1
    if 't' in s[:k] and 't' in s[k:]:
        count += 1
    if 'u' in s[:k] and 'u' in s[k:]:
        count += 1
    if 'v' in s[:k] and 'v' in s[k:]:
        count += 1
    if 'w' in s[:k] and 'w' in s[k:]:
        count += 1
    if 'x' in s[:k] and 'x' in s[k:]:
        count += 1
    if 'y' in s[:k] and 'y' in s[k:]:
        count += 1
    if 'z' in s[:k] and 'z' in s[k:]:
        count += 1
    return count
n = int(input())
s = input()
ans = 0
for i in range(1,n-1):
    temp = al_cnt(i,s)
    ans = max(ans,temp)
print(ans)
