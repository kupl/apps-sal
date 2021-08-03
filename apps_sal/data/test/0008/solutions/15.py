s = input()
ans = 2
s1 = s[0:2]
s2 = s[3:5]
s3 = s[6:8]


def func(inp):
    ans = 2
    num = int(inp[0])
    c = inp[1]
    ans = min(ans, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num + 2) + c) != -1))
    ans = min(ans, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num - 1) + c) != -1))
    ans = min(ans, 2 - int(s.find(str(num - 1) + c) != -1) - int(s.find(str(num - 2) + c) != -1))
    ans = min(ans, 3 - s.count(inp))
    return ans


ans = min(ans, func(s1))
ans = min(ans, func(s2))
ans = min(ans, func(s3))
print(ans)
