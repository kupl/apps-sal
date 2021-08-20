(num_skills, improvement) = list(map(int, input().split()))
skills = list(map(int, input().split()))
skills.sort(key=lambda skill: 10 - skill % 10)
for (i, skill) in enumerate(skills):
    if skill == 100:
        continue
    delta = min(improvement, 10 - skill % 10)
    skills[i] += delta
    improvement -= delta
    if improvement == 0:
        break
for (i, skill) in enumerate(skills):
    delta = min(improvement, 100 - skill)
    skills[i] += delta
    improvement -= delta
    if improvement == 0:
        break
result = 0
for skill in skills:
    result += skill // 10
print(result)
