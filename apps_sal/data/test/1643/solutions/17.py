s = input()

res = ["0"] * len(s)
min_dif = 0
length = len(s)

for i in range(length):
    if s[length - i - 1] == "0":
        min_dif = min([-1, min_dif - 1])
    else:
        if min_dif < 0:
            res[length - i - 1] = "1"
        min_dif = min([1, min_dif + 1])
print("".join(res))
