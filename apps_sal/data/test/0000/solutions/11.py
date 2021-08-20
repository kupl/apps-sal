def solve(s):
    if s.find('[') == -1:
        return -1
    s = s[s.find('['):]
    if s.find(':') == -1:
        return -1
    s = s[s.find(':') + 1:]
    if s.find(']') == -1:
        return -1
    s = s[:s.rfind(']')]
    if s.find(':') == -1:
        return -1
    s = s[:s.rfind(':')]
    return s.count('|') + 4


s = input()
print(solve(s))
