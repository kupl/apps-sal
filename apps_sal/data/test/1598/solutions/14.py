s = input()

res = ""
min_dif = 0

for i in range(len(s)):
    if s[len(s)-i-1] == "0":
        res = "0"+res
        min_dif = min([-1, min_dif-1])
    else:
        if min_dif >= 0: res = "0"+res
        else: res = "1"+res
        min_dif = min([1, min_dif+1])
print(res)
