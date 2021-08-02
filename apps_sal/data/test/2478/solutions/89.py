n = int(input())
s = input()
counter_l = 0
pairs = 0
double_check = set()

for i in range(n):
    if s[i] == "(":
        counter_l += 1
        for j in range(i + 1, n):
            if s[j] == ")" and j not in double_check:
                pairs += 1
                double_check.add(j)
                break
counter_r = n - counter_l
s = s + ")" * (counter_l - pairs)
s = "(" * (counter_r - pairs) + s

print(s)
