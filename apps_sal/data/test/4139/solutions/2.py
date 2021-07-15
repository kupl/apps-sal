n = int(input())
ans = 0
list_N = [["3", "5", "7"]]

for i in range(2, 10):
    d = []
    for a in list_N[-1]:
        for b in ["3", "5", "7"]:
            k = b + a
            if n >= int(k) and "3" in k and "5" in k and "7" in k:
                ans += 1
            d.append(k)
    list_N.append(d)

print(ans)
