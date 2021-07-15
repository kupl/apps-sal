n = int(input())
s = input()

curr_left = s[0]
curr_right = s[-1]
s_left = 0
s_right = 0
i = 0
while curr_left == s[i]:
    s_left +=1
    i+=1
i = len(s)-1
while curr_right == s[i]:
    s_right +=1
    i+=-1

if curr_left == curr_right:
    print((s_left+1)*(s_right+1)%998244353)
else:
    print((s_left + s_right + 1)%998244353)
