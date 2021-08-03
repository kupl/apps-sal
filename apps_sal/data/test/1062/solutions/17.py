# compute hamming distance
# mark indexes that differ
# m_benefit=0,s_i,s_j
# for each i in index
#   for each j in i+1
#       swap i & j and see what is the benefit
#       if benefit > m_benefit:
#           m_ben=ben
#           record m_i and m_j
# if m_ben = 0 then -1 -1
# else distance-benefit and print s_i+1&s_j+1
diff = []
wrong_t = {}


def distance(n, s, t):
    count = 0
    for i in range(n):
        if s[i] != t[i]:
            diff.append(i)
            wrong_t[t[i]] = i
            count += 1
    return count


def minDistance():
    m_ben = 0
    m_i = -2
    m_j = -2
    for i in diff:
        v = wrong_t[s[i]] if (s[i] in wrong_t) else None
        if v != None:
            m_ben = 1
            m_i = i
            m_j = v
            if s[v] == t[i]:
                return (2, i, v)
    return (m_ben, m_i, m_j)


n = int(input())
s = input()
t = input()
d = distance(n, s, t)
m_ben, m_i, m_j = minDistance()
print(d - m_ben)
print("{0} {1}".format(m_i + 1, m_j + 1))
