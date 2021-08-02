n = int(input())
if n % 2:
    print(":(")
    return
s = [c for c in input()]
if s[0] == ")" or s[-1] == "(":
    print(":(")
    return
s[0] = "("
s[-1] = ")"

count_open = s.count("(")
count_close = s.count(")")
half = n // 2
if count_close > half or count_open > half:
    print(":(")
    return
available = half - count_open
current = 0
for i, x in enumerate(s):
    if x == "(":
        current += 1
    elif x == ")":
        current -= 1
    else:
        if available:
            current += 1
            available -= 1
            s[i] = "("
        else:
            current -= 1
            s[i] = ")"
    if current == 0 and i != n - 1:
        print(":(")
        return

print("".join(s))
