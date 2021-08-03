def solve(s):
    if s.find('[') == -1:
        return -1
    s = s[s.find('['):]
    # print(s)
    if s.find(':') == -1:
        return -1
    s = s[s.find(':') + 1:]
    # print(s)
    if s.find(']') == -1:
        return -1
    s = s[:s.rfind(']')]
    # print(s)
    if s.find(':') == -1:
        return -1
    s = s[:s.rfind(':')]
    # print(s)
    return s.count('|') + 4


s = input()
print(solve(s))
