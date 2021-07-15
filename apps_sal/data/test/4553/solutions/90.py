a, b = map(int, input().split())
s = list(input())
def f():
    for i in range(len(s)):
        if i == a:
            if s[i] != "-":
                return "No"
        else:
            if s[i] == "-":
                return "No"
    return "Yes"
print(f())
