n = int(input())
list_s = list(input())
for i in range(0, len(list_s)):
    tmp = ord(list_s[i]) + n
    if tmp > ord("Z"):
        tmp -= 26
    list_s[i] = chr(tmp)
print("".join(list_s))
