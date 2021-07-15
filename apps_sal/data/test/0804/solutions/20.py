s = input()
n = int(input())
m_set = set()
for i in range(len(s)):
    m_set.add(s[i])
if n > len(s):
    print("impossible")
else:
    print(max(0, n - len(m_set)))
