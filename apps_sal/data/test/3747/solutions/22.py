s = "Bulbasaur"
lst = input().strip()
cnt1 = [0] * 26
cnt2 = [0] * 26
for i in range(len(lst)):
    if lst[i] >= 'a' and lst[i] <= 'z':
        cnt1[ord(lst[i]) - ord('a')] += 1
    else:
        cnt2[ord(lst[i]) - ord('A')] += 1
answer = 1e6
for i in range(1, len(s)):
    answer = min(answer, cnt1[ord(s[i]) - ord('a')])
answer = min(answer, cnt1[0] // 2, cnt1[ord('u') - 97] // 2)
print(min(answer, cnt2[1]))
