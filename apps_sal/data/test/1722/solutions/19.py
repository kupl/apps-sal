n = int(input())
dict1 = {}
for i in range(n):
    s = str(input())
    try:
        dict1[s[0]] += 1
    except:
        KeyError
        dict1[s[0]] = 1
ans = 0
for i in list(dict1.keys()):
    if(dict1[i] > 2):
        val1 = dict1[i] // 2
        val2 = dict1[i] // 2 + dict1[i] % 2
        if(val1 > 0):
            ans += (val1 * (val1 - 1)) // 2
        if(val2 > 0):
            ans += (val2 * (val2 - 1)) // 2
print(ans)
