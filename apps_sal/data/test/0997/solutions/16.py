l = input()
l = l.replace(";", ",")
l = l.split(",")
nums = []
alpha = []

for i in l:
    try:
        num = int(i)
        if str(num) == i:
            nums.append(str(num))
        else:
            alpha.append(i)
    except:
        alpha.append(i)

if len(nums) == 0:
    print("-")
else:
    print("\"" + ",".join(nums) + "\"")
if len(alpha) == 0:
    print("-")
else:
    print("\"" + ",".join(alpha) + "\"")
