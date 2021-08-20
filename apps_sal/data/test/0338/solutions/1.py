maximum = input()
m_int = list(map(int, input().split()))
size = list(map(int, input().split()))
x = size[0]
y = size[1]
beginner = []
intermediate = []
for i in range(len(m_int)):
    beginner.append(m_int[i])
    if sum(beginner) > y or sum(m_int[i + 1:]) < x:
        del beginner[-1]
        break
for j in range(len(beginner), len(m_int)):
    intermediate.append(m_int[j])
if (sum(intermediate) < x or sum(intermediate) > y) or (sum(beginner) < x or sum(beginner) > y):
    passing_rate = 0
else:
    passing_rate = i + 1
print(passing_rate)
