s = input()
if len(s) == 1:
    ans = 0
else:
    ans_w = sum([ 1 for i in s[::2] if i != '1']) + sum([ 1 for i in s[1::2] if i != '0'])
    ans_b = sum([ 1 for i in s[::2] if i != '0']) + sum([ 1 for i in s[1::2] if i != '1'])
    ans = min([ans_w, ans_b])
print(ans) 
