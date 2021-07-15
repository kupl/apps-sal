s = list(input())
def slv(i):
    if i == 1 or i == 9:
        return 10-i
    else:
        return i
print(str(slv(int(s[0])))+str(slv(int(s[1])))+str(slv(int(s[2]))))
