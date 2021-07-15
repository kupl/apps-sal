list_s = list(input())
list_t = list(input())
n = len(list_s)
for i in range(0, n):
    if "".join(list_s) == "".join(list_t):
        print("Yes")
        return
    list_s.insert(0, list_s[n - 1])
    list_s.pop(-1)
print("No")
