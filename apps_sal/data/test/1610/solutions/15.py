sa = input().split(' ')
nums = int(sa[0])
decs = int(sa[1])
string = ''
for x in range(nums, nums - decs, -1):
    string += str(x)
    string += ' '
for x in range(1, nums - decs + 1):
    string += str(x)
    string += ' '
print(string.strip())
