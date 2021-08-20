(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
person_to_skill = {}
skill_to_numMentor = {}
person_to_numMentor = {}
for person in range(len(arr)):
    person_to_skill[person] = arr[person]
arr = sorted(arr)
temp = -1
for i in range(len(arr)):
    if arr[i] != temp:
        skill_to_numMentor[arr[i]] = i
        temp = arr[i]
for person in range(n):
    person_to_numMentor[person] = skill_to_numMentor[person_to_skill[person]]
for quarrel in range(k):
    (p1, p2) = list(map(int, input().split()))
    if person_to_skill[p1 - 1] > person_to_skill[p2 - 1]:
        person_to_numMentor[p1 - 1] -= 1
    if person_to_skill[p2 - 1] > person_to_skill[p1 - 1]:
        person_to_numMentor[p2 - 1] -= 1
s = ''
s += str(person_to_numMentor[0])
for i in range(1, n):
    s += ' ' + str(person_to_numMentor[i])
print(s)
