s = input()
n = int(input())
f = True


def is_sim(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i].lower() == s2[i].lower() or s1[i] + s2[i] in ['O0', '0O', 'o0', '0o'] or (s1[i] in ['1', 'l', 'I', 'i', 'L'] and s2[i] in ['1', 'l', 'I', 'i', 'L']):
            pass
        else:
            return False
    return True


for i in range(n):
    t = input()
    if is_sim(s, t):
        f = False
print('Yes' if f else 'No')
