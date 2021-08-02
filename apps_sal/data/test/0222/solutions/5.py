def valid_int(n):
    return int(round(n ** 0.5)) ** 2 == n


def valid(s):
    return valid_int(int(s))


def no_start_zero(s):
    return s[0] != '0'


n = input()


def adj(s):
    if len(s) <= 1: return []
    for i in range(len(s)):
        ss = s[:i] + s[i + 1:]
        if no_start_zero(ss):
            yield ss


q = [n]
seen = set()

while q:
    node = q.pop(0)
    if valid(node):
        print(len(n) - len(node))
        return
    for child in adj(node):
        if child not in seen:
            seen.add(child)
            q.append(child)
print(-1)
