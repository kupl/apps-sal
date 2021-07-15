s = input()

acgt = ['A','C','G','T']
i = 0
max_ans = 0
curr_ans = 0

while(i < len(s)):
    if s[i] in acgt:
        curr_ans += 1
    else:
        max_ans = max(max_ans, curr_ans)
        curr_ans = 0
    i += 1
max_ans = max(max_ans, curr_ans)
print(max_ans)
