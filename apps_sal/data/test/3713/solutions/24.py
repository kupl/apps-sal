def non_standard(s):
    result = 1
    for i in range(1, len(s)):
        result += (s[i] != s[i - 1])
    return min(result + 2, len(s))


m = int(input())
t = input()
print(non_standard(t))
