n = int(input())
s = input()
s1 = s[:n // 2]
s2 = s[n // 2:]
sum1 = sum(map(int, filter(str.isdigit, s1)))
sum2 = sum(map(int, filter(str.isdigit, s2)))
free1 = s1.count("?")
free2 = s2.count("?")
ans = ""
if free1 == free2:
    if sum1 == sum2:
        ans = "Bicarp"
    else:
        ans = "Monocarp"
else:
    if sum1 > sum2:
        free1, free2 = free2, free1
        sum1, sum2 = sum2, sum1
    if free1 <= free2:
        ans = "Monocarp"
    else:
        if (free1 - free2) // 2 * 9 == sum2 - sum1:
            ans = "Bicarp"
        else:
            ans = "Monocarp"
print(ans)
