import sys
n = int(sys.stdin.readline().strip())
ss = [sys.stdin.readline().strip() for _ in range(n)]

# def compare_and_truncate(s1, s2):
#     if s1 == s2:
#         return s1
#     min_l = min(len(s1), len(s2))
#     for i in range(min_l):
#         if ord(s1[i]) < ord(s2[i]):
#             return s1
#         elif ord(s1[i]) > ord(s2[i]):
#             return s1[:i]
#     return s1[:min_l]


def compare_and_truncate(s1, s2):
    if s1 > s2:
        i = 0
        while i < len(s2) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
    return s1


for i in range(len(ss) - 2, -1, -1):
    ss[i] = compare_and_truncate(ss[i], ss[i + 1])

ans = ""
for s in ss:
    ans += s + "\n"

sys.stdout.write(ans)
