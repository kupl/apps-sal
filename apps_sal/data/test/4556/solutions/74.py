s = input()
strs = s.split(' ')
c = strs[1][0].upper()

ans = "{}{}{}".format(strs[0][0], c, strs[2][0])
print(ans)
