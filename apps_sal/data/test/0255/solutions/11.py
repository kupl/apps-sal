
R = lambda : map(int, input().split())

n = int(input())
m_skills = sorted(list(R()))

m = int(input())
w_skills = sorted(list(R()))

N = max(m,n)
j_list = []
i_list = []
res    = 0
for i in range(n):
    for j in range(m):
        if abs(m_skills[i] - w_skills[j]) in [0,1] and j not in j_list:
            j_list.append(j)
            res += 1
            break

print(res)
