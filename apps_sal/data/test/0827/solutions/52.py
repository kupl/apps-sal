n = int(input())
t = input()


if "111" in t or "00" in t or "010" in t:
    ans = 0
elif t == "1":
    ans = 2 * (10 ** 10)
elif t == "11":
    ans = 10 ** 10
elif t[-1] == "0":
    ans = 10 ** 10 - t.count("0") + 1
elif t[-1] == "1":
    ans = 10 ** 10 - t.count("0")
    
print(ans)

