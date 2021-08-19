s = input()
arr = []
for i in range(0, len(s) - 2):
    arr.append(abs(753 - int(str(s[i]) + str(s[i + 1]) + str(s[i + 2]))))
print(min(arr))
